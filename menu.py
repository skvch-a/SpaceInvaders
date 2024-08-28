import pygame
from constants import *

class Menu:
    def __init__(self):
        self.background_img = pygame.image.load("Assets/Graphics/UI/Background.png")
        self.background_img = pygame.transform.scale(self.background_img, (SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + OFFSET * 2))
        self.background_rect = self.background_img.get_rect()

        self.play_button_img = pygame.image.load("Assets/Graphics/UI/StartButton.png")
        self.play_button_img = pygame.transform.scale(self.play_button_img, (360, 80))
        self.play_button_rect = self.play_button_img.get_rect(center=((SCREEN_WIDTH + OFFSET) / 2, SCREEN_HEIGHT / 2))

        self.leaderboard_button_img = pygame.image.load("Assets/Graphics/UI/LeaderboardButton.png")
        self.leaderboard_button_img = pygame.transform.scale(self.leaderboard_button_img, (360, 80))
        self.leaderboard_button_rect = self.leaderboard_button_img.get_rect(center=((SCREEN_WIDTH + OFFSET) / 2, SCREEN_HEIGHT / 2 + 110))

    def draw(self, screen):
        screen.blit(self.background_img, self.background_rect)
        screen.blit(self.play_button_img, self.play_button_rect)
        screen.blit(self.leaderboard_button_img, self.leaderboard_button_rect)