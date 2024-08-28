import pygame
import sys
from random import randint

class EventHandler:
    def __init__(self, game, menu):
        self.game = game
        self.menu = menu
        self.shoot_laser_event = pygame.USEREVENT
        pygame.time.set_timer(self.shoot_laser_event, 300)
        self.mystery_ship_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.mystery_ship_event, randint(4000, 8000))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.game.run:
                if event.type == self.shoot_laser_event:
                    self.game.alien_fleet.shoot()
                if event.type == self.mystery_ship_event:
                    self.game.create_mystery_ship()
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.menu.play_button_rect.collidepoint(event.pos):
                        self.game.start()
        if self.game.run:
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
        self.process_user_input()
        self.game.alien_fleet.move()
        self.game.alien_fleet.lasers_group.update()
        self.game.player_ship.lasers_group.update()
        self.game.mystery_ship_group.update()
        self.game.check_for_collisions()