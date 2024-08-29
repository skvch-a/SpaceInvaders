import pygame
from constants import *


class GameOverScreen:
    def __init__(self, color):
        self.font = pygame.font.Font(FONT_PATH, 64)
        self.color = color
        screen_size = (SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + OFFSET * 2)
        self.text_surface = self.font.render("GAME OVER!", False, self.color)
        self.text_rect = self.text_surface.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))

    def draw(self, screen):
        screen.blit(self.text_surface, self.text_rect)