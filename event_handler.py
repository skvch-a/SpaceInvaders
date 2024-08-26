import pygame
import sys
from random import randint

class EventHandler:
    def __init__(self, game):
        self.game = game
        self.shoot_laser_event = pygame.USEREVENT
        pygame.time.set_timer(self.shoot_laser_event, 300)
        self.mystery_ship_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.mystery_ship_event, randint(4000, 8000))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == self.shoot_laser_event and self.game.run:
                self.game.alien_shoot_laser()

            if event.type == self.mystery_ship_event and self.game.run:
                self.game.create_mystery_ship()
                pygame.time.set_timer(self.mystery_ship_event, randint(4000, 8000))

        self.update_game_objects()

    def process_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.game.player_ship.move_right()
        if keys[pygame.K_LEFT]:
            self.game.player_ship.move_left()
        if keys[pygame.K_SPACE]:
            self.game.player_ship.shoot()

    def update_game_objects(self):
        if self.game.run:
            self.process_user_input()
            self.game.player_ship.laser_gun.update()
            self.game.move_aliens()
            self.game.alien_lasers_group.update()
            self.game.mystery_ship_group.update()
            self.game.check_for_collisions()