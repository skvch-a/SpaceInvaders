import pygame

from constants import TITLE
from event_handler import EventHandler
from renderer import Renderer
from game import Game
from menu import Menu

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()
    game = Game()
    menu = Menu()
    renderer = Renderer(game, menu)
    event_handler = EventHandler(game, menu)

    while True:
        event_handler.handle_events()
        renderer.render()
        pygame.display.update()
        FPS = 1
        if game.is_running():
            FPS = game.get_fps()
        clock.tick(FPS)

