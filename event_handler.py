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