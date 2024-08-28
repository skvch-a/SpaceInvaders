import pygame

from constants import *
from alien_fleet import AlienFleet
from leaderboard import update_leaderboard, get_max_score
from player_ship import PlayerShip
from mystery_ship import MysteryShip
from obstacle import Obstacle


class Game:
    def __init__(self):
        self.run = False
        self.player_ship = None
        self.obstacles = None
        self.alien_fleet = None
        self.mystery_ship_group = None
        self.lives = None
        self.score = None
        self.highscore = None
        self.explosion_sound = None

    def start(self):
        self.run = True
        self.player_ship = PlayerShip()
        self.obstacles = self.create_obstacles()
        self.alien_fleet = AlienFleet()
        self.mystery_ship_group = pygame.sprite.GroupSingle()
        self.lives = LIVES_COUNT
        self.score = 0
        self.highscore = get_max_score()
        self.explosion_sound = pygame.mixer.Sound("Assets/Audio/explosion.ogg")
        pygame.mixer.music.load("Assets/Audio/music.ogg")
        pygame.mixer.music.play(-1)

    def stop(self):
        self.run = False
        pygame.mixer.music.stop()

    def draw_obstacles(self, screen):
        for obstacle in self.obstacles:
            obstacle.blocks_group.draw(screen)

    def update(self):
        self.alien_fleet.move()
        self.alien_fleet.lasers_group.update()
        self.player_ship.lasers_group.update()
        self.mystery_ship_group.update()
        self.check_for_collisions()

    def create_mystery_ship(self):
        self.mystery_ship_group.add(MysteryShip())

    def check_player_ship_lasers_collisions(self):
        if self.player_ship.lasers_group:
            for laser_sprite in self.player_ship.lasers_group:

                aliens_hit = pygame.sprite.spritecollide(laser_sprite, self.alien_fleet, True)
                if aliens_hit:
                    self.explosion_sound.play()
                    for alien in aliens_hit:
                        self.score += alien.type * BASIC_ALIEN_SCORE
                        update_leaderboard(self.score)
                        laser_sprite.kill()

                if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, True):
                    self.score += MYSTERY_SHIP_SCORE
                    self.explosion_sound.play()
                    update_leaderboard(self.score)
                    laser_sprite.kill()

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

    def check_alien_fleet_lasers_collisions(self):
        if self.alien_fleet.lasers_group:
            for laser_sprite in self.alien_fleet.lasers_group:
                if pygame.sprite.collide_rect(laser_sprite, self.player_ship):
                    laser_sprite.kill()
                    self.lives -= 1
                    if self.lives == 0:
                        self.stop()

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

    def check_for_collisions(self):
        self.check_player_ship_lasers_collisions()
        self.check_alien_fleet_lasers_collisions()
        if self.alien_fleet:
            for alien in self.alien_fleet:
                for obstacle in self.obstacles:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)

                if pygame.sprite.collide_rect(alien, self.player_ship):
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

