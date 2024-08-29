import pygame

from constants import *
from alien_fleet import AlienFleet
from leaderboard import update_leaderboard, get_max_score
from player_ship import PlayerShip
from mystery_ship import MysteryShip
from shelter import Shelter


class Game:
    def __init__(self):
        self._run = False
        self._FPS = None
        self._level_number = None
        self._level_color = None
        self._player_ship = None
        self._shelters = None
        self._alien_fleet = None
        self._mystery_ship_group = None
        self._lives = None
        self._score = None
        self._highscore = None
        self._explosion_sound = None
        self._background_image = None
        self._background_rect = None

    def start(self):
        self._run = True
        self._FPS = START_FPS
        self._level_number = 1
        self._level_color = self.get_level_color()
        self._player_ship = PlayerShip(self._level_color)
        self._shelters = self.create_shelters()
        self._alien_fleet = AlienFleet(self._level_color)
        self._mystery_ship_group = pygame.sprite.GroupSingle()
        self._lives = LIVES_COUNT
        self._score = 0
        self._highscore = get_max_score()
        self._explosion_sound = pygame.mixer.Sound(EXPLOSION_SOUND_PATH)
        pygame.mixer.music.load(GAME_MUSIC_PATH)
        pygame.mixer.music.set_volume(GAME_MUSIC_VOLUME)
        pygame.mixer.music.play(-1)

    def stop(self):
        self._run = False
        update_leaderboard(self._score, self._level_number)
        pygame.mixer.music.stop()

    def next_level(self):
        self._score += 500
        self._level_number += 1
        self._FPS += 15
        self._level_color = self.get_level_color()
        self._player_ship = PlayerShip(self._level_color)
        self._shelters = self.create_shelters()
        self._alien_fleet = AlienFleet(self._level_color)
        self._mystery_ship_group = pygame.sprite.GroupSingle()
        self._lives = LIVES_COUNT

    def get_fps(self):
        return self._FPS

    def get_level_number(self):
        return self._level_number

    def get_level_color(self):
        return LEVEL_COLORS[(self._level_number - 1) % len(LEVEL_COLORS)]

    def is_running(self):
        return self._run

    def get_lives(self):
        return self._lives

    def get_score(self):
        return self._score

    def get_player_ship(self):
        return self._player_ship

    def alien_fleet_shoot(self):
        self._alien_fleet.shoot()

    def draw_game_objects(self, screen):
        self._player_ship.draw_ship_and_lasers(screen)
        for obstacle in self._shelters:
            obstacle.blocks_group.draw(screen)
        self._alien_fleet.draw_fleet_and_lasers(screen)
        self._mystery_ship_group.draw(screen)

    def update(self):
        if len(self._alien_fleet) == 0:
            self.next_level()
        else:
            self._alien_fleet.move()
            self._alien_fleet.update_lasers()
            self._player_ship.update_lasers()
            self._mystery_ship_group.update()
            self.check_for_collisions()

    def launch_mystery_ship(self):
        self._mystery_ship_group.add(MysteryShip(self._level_color))

    def check_player_ship_lasers_collisions(self):
        if self._player_ship.get_lasers():
            for laser_sprite in self._player_ship.get_lasers():

                aliens_hit = pygame.sprite.spritecollide(laser_sprite, self._alien_fleet, True)
                if aliens_hit:
                    self._explosion_sound.play()
                    for alien in aliens_hit:
                        self._score += alien.get_type() * BASIC_ALIEN_SCORE
                        laser_sprite.kill()

                if pygame.sprite.spritecollide(laser_sprite, self._mystery_ship_group, True):
                    self._score += MYSTERY_SHIP_SCORE
                    self._explosion_sound.play()
                    laser_sprite.kill()

                for obstacle in self._shelters:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

    def check_alien_fleet_lasers_collisions(self):
        if self._alien_fleet.get_lasers():
            for laser_sprite in self._alien_fleet.get_lasers():
                if pygame.sprite.collide_rect(laser_sprite, self._player_ship):
                    laser_sprite.kill()
                    self._lives -= 1
                    if self._lives == 0:
                        self.stop()

                for obstacle in self._shelters:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

    def check_for_collisions(self):
        self.check_player_ship_lasers_collisions()
        self.check_alien_fleet_lasers_collisions()
        if self._alien_fleet:
            for alien in self._alien_fleet:
                for obstacle in self._shelters:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)

                if pygame.sprite.collide_rect(alien, self._player_ship):
                    self.stop()

    def create_shelters(self):
        shelter_width = len(OBSTACLE_GRID[0]) * 3
        gap = (SCREEN_WIDTH + OFFSET - (4 * shelter_width)) / 5
        shelters = []
        for i in range(4):
            pos_x = (i + 1) * gap + i * shelter_width
            shelter = Shelter(self._level_color, pos_x, SCREEN_HEIGHT - 100)
            shelters.append(shelter)
        return shelters

