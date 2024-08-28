import pygame
import sys
from random import randint

class EventHandler:
    def __init__(self, game, menu):
        self._game = game
        self._menu = menu

        self.shoot_laser_event = pygame.USEREVENT
        pygame.time.set_timer(self.shoot_laser_event, 300)
        self.mystery_ship_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.mystery_ship_event, randint(4000, 8000))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self._game.is_running():
                if event.type == self.shoot_laser_event:
                    self._game.alien_fleet_shoot()
                if event.type == self.mystery_ship_event:
                    self._game.create_mystery_ship()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self._game.stop()
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self._menu.play_button_rect.collidepoint(event.pos):
                        self._game.start()

        if self._game.is_running():
            self.update_game_objects()

    def handle_player_controls(self):
        keys = pygame.key.get_pressed()
        player_ship = self._game.get_player_ship()
        if keys[pygame.K_RIGHT]:
            player_ship.move_right()
        if keys[pygame.K_LEFT]:
            player_ship.move_left()
        if keys[pygame.K_SPACE]:
            player_ship.shoot()

    def update_game_objects(self):
        self.handle_player_controls()
        self._game.update()