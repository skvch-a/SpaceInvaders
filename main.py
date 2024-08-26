import pygame
from constants import *
from event_handler import EventHandler
from visualizer import Visualizer
from game import Game


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()
    game = Game()
    visualizer = Visualizer(game)
    event_handler = EventHandler(game)

    while True:
        event_handler.handle_events()
        visualizer.visualize()
        pygame.display.update()
        clock.tick(FPS)
