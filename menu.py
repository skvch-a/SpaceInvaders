import pygame
from leaderboard import draw_leaderboard
from constants import *


class Menu:
    def __init__(self):
        self.background_img = pygame.image.load("Assets/Graphics/UI/Background.png")
        self.background_rect = self.background_img.get_rect()

        self.play_button_img = pygame.image.load("Assets/Graphics/UI/StartButton.png")
        self.play_button_rect = self.play_button_img.get_rect(center=((SCREEN_WIDTH + OFFSET) / 2, SCREEN_HEIGHT / 2))

    def draw(self, screen):
        screen.blit(self.background_img, self.background_rect)
        screen.blit(self.play_button_img, self.play_button_rect)
        draw_leaderboard(screen)
