import pygame

from constants import *
from alien_fleet import AlienFleet
from leaderboard import update_leaderboard, get_max_score
from player_ship import PlayerShip
from mystery_ship import MysteryShip
from obstacle import Obstacle


class Game:
    def __init__(self):
        self._run = False
        self._player_ship = None
        self._obstacles = None
        self._alien_fleet = None
        self._mystery_ship_group = None
        self._lives = None
        self._score = None
        self._highscore = None
        self._explosion_sound = None

    def is_running(self):
        return self._run

    def get_lives(self):
        return self._lives

    def get_player_ship_image(self):
        return self._player_ship.get_image()

    def get_player_ship_rect(self):
        return self._player_ship.get_rect()

    def get_score(self):
        return self._score

    def draw_player_ship_and_lasers(self, screen):
        self._player_ship.draw_ship_and_lasers(screen)

    def draw_alien_fleet_and_lasers(self, screen):
        self._alien_fleet.draw_fleet_and_lasers(screen)

    def draw_mystery_ship(self, screen):
        self._mystery_ship_group.draw(screen)

    def start(self):
        self._run = True
        self._player_ship = PlayerShip()
        self._obstacles = self.create_obstacles()
        self._alien_fleet = AlienFleet()
        self._mystery_ship_group = pygame.sprite.GroupSingle()
        self._lives = LIVES_COUNT
        self._score = 0
        self._highscore = get_max_score()
        self._explosion_sound = pygame.mixer.Sound("Assets/Audio/explosion.ogg")
        pygame.mixer.music.load("Assets/Audio/music.ogg")
        pygame.mixer.music.play(-1)

    def stop(self):
        self._run = False
        pygame.mixer.music.stop()

    def draw_obstacles(self, screen):
        for obstacle in self._obstacles:
            obstacle.blocks_group.draw(screen)

    def update(self):
        self._alien_fleet.move()
        self._alien_fleet.update_lasers()
        self._player_ship.update_lasers()
        self._mystery_ship_group.update()
        self.check_for_collisions()

    def create_mystery_ship(self):
        self._mystery_ship_group.add(MysteryShip())

    def check_player_ship_lasers_collisions(self):
        if self._player_ship.get_lasers():
            for laser_sprite in self._player_ship.get_lasers():

                aliens_hit = pygame.sprite.spritecollide(laser_sprite, self._alien_fleet, True)
                if aliens_hit:
                    self._explosion_sound.play()
                    for alien in aliens_hit:
                        self._score += alien.type * BASIC_ALIEN_SCORE
                        update_leaderboard(self._score)
                        laser_sprite.kill()

                if pygame.sprite.spritecollide(laser_sprite, self._mystery_ship_group, True):
                    self._score += MYSTERY_SHIP_SCORE
                    self._explosion_sound.play()
                    update_leaderboard(self._score)
                    laser_sprite.kill()

                for obstacle in self._obstacles:
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

                for obstacle in self._obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

    def check_for_collisions(self):
        self.check_player_ship_lasers_collisions()
        self.check_alien_fleet_lasers_collisions()
        if self._alien_fleet:
            for alien in self._alien_fleet:
                for obstacle in self._obstacles:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)

                if pygame.sprite.collide_rect(alien, self._player_ship):
                    self.stop()

    @staticmethod
    def create_obstacles():
        obstacle_width = len(OBSTACLE_GRID[0]) * 3
        gap = (SCREEN_WIDTH + OFFSET - (4 * obstacle_width)) / 5
        obstacles = []
        for i in range(4):
            pos_x = (i + 1) * gap + i * obstacle_width
            obstacle = Obstacle(pos_x, SCREEN_HEIGHT - 100)
            obstacles.append(obstacle)
        return obstacles

