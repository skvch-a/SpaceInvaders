import pygame
from constants import *
from event_handler import EventHandler
from game_renderer import GameRenderer
from game import Game
from menu import Menu

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()
    game = Game()
    menu = Menu()
    renderer = GameRenderer(game, menu)
    event_handler = EventHandler(game, menu)

    while True:
        event_handler.handle_events()
        renderer.render()
        pygame.display.update()
        clock.tick(FPS)
