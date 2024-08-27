import pygame
from pygame.sprite import GroupSingle

from alien_fleet import AlienFleet
from constants import *
from player_ship import PlayerShip
from obstacle import Obstacle
from obstacle import OBSTACLE_GRID
from mystery_ship import MysteryShip


class Game:
    def __init__(self):
        self.player_ship = PlayerShip()
        self.obstacles = self.create_obstacles()
        self.alien_fleet = AlienFleet()
        self.mystery_ship_group = GroupSingle()
        self.lives = LIVES_COUNT
        self.run = True
        self.score = 0
        self.highscore = 0
        self.explosion_sound = pygame.mixer.Sound("Assets/Audio/explosion.ogg")
        self.load_highscore()
        pygame.mixer.music.load("Assets/Audio/music.ogg")
        pygame.mixer.music.play(-1)

    def create_mystery_ship(self):
        self.mystery_ship_group.add(MysteryShip())


    def create_obstacles(self):
        obstacle_width = len(OBSTACLE_GRID[0]) * 3
        gap = (SCREEN_WIDTH + OFFSET - (4 * obstacle_width)) / 5
        obstacles = []
        for i in range(4):
            offset_x = (i + 1) * gap + i * obstacle_width
            obstacle = Obstacle(offset_x, SCREEN_HEIGHT - 100)
            obstacles.append(obstacle)
        return obstacles

    def check_for_collisions(self):
        # Spaceship
        if self.player_ship.lasers_group:
            for laser_sprite in self.player_ship.lasers_group:

                aliens_hit = pygame.sprite.spritecollide(laser_sprite, self.alien_fleet, True)
                if aliens_hit:
                    self.explosion_sound.play()
                    for alien in aliens_hit:
                        self.score += alien.type * 100
                        self.check_for_highscore()
                        laser_sprite.kill()

                if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, True):
                    self.score += 500
                    self.explosion_sound.play()
                    self.check_for_highscore()
                    laser_sprite.kill()

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

        # Alien Lasers
        if self.alien_fleet.lasers_group:
            for laser_sprite in self.alien_fleet.lasers_group:
                if pygame.sprite.collide_rect(laser_sprite, self.player_ship):
                    laser_sprite.kill()
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over()

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

        if self.alien_fleet:
            for alien in self.alien_fleet:
                for obstacle in self.obstacles:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)

                if pygame.sprite.collide_rect(alien, self.player_ship):
                    self.game_over()

    def game_over(self):
        self.run = False

    def check_for_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score

            with open("highscore.txt", "w") as file:
                file.write(str(self.highscore))

    def load_highscore(self):
        try:
            with open("highscore.txt", "r") as file:
                self.highscore = int(file.read())
        except FileNotFoundError:
            self.highscore = 0
