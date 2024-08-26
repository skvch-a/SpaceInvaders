import sys
import pygame
from event_handler import EventHandler
from visualizer import Visualizer
from constants import *
from game import Game

pygame.init()
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)
visualizer = Visualizer(game)

event_handler = EventHandler(game)

while True:
    event_handler.handle_events()

    if game.run:
        game.update()

    visualizer.visualize()
    pygame.display.update()
    clock.tick(60)
