import sys
import pygame
import random
from visualizer import Visualizer
from constants import *
from game import Game

pygame.init()
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)
visualizer = Visualizer(game)

shoot_laser_event = pygame.USEREVENT
pygame.time.set_timer(shoot_laser_event, 300)

mystery_ship_event = pygame.USEREVENT + 1
pygame.time.set_timer(mystery_ship_event, random.randint(4000, 8000))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == shoot_laser_event and game.run:
            game.alien_shoot_laser()

        if event.type == mystery_ship_event and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(mystery_ship_event, random.randint(4000, 8000))

    if game.run:
        game.update()

    visualizer.visualize()
    pygame.display.update()
    clock.tick(60)
