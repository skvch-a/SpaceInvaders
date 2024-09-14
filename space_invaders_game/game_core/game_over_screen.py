from ..constants import FONT_PATH, GAME_OVER_FONT_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

import pygame


class GameOverScreen:
    def __init__(self, color):
        self.font = pygame.font.Font(FONT_PATH, GAME_OVER_FONT_SIZE)
        self.color = color
        self.text_surface = self.font.render("GAME OVER!", False, self.color)
        self.text_rect = self.text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def draw(self, screen) -> None:
        screen.blit(self.text_surface, self.text_rect)