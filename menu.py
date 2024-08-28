import pygame
import json
from constants import *


class Menu:
    def __init__(self):
        self.background_img = pygame.image.load("Assets/Graphics/UI/Background.png")
        self.background_rect = self.background_img.get_rect()

        self.play_button_img = pygame.image.load("Assets/Graphics/UI/StartButton.png")
        self.play_button_rect = self.play_button_img.get_rect(center=((SCREEN_WIDTH + OFFSET) / 2, SCREEN_HEIGHT / 2))

        self.leaderboard = self.load_leaderboard()
        self.font = pygame.font.Font('Assets/Font/monogram.ttf', 50)

    def draw(self, screen):
        screen.blit(self.background_img, self.background_rect)
        screen.blit(self.play_button_img, self.play_button_rect)
        self.display_leaderboard(screen)

    def display_leaderboard(self, screen):
        title_text = self.font.render("HIGH SCORES: ", True, (255, 255, 255))
        screen.blit(title_text, ((SCREEN_WIDTH - title_text.get_width() + OFFSET) / 2, 550))

        y_offset = 600
        for index, entry in enumerate(self.leaderboard):
            name = entry.get('name')
            score = entry.get('score')
            record_text = f"{index + 1}. {name} - {score}"
            text_surface = self.font.render(record_text, True, (255, 255, 255))
            screen.blit(text_surface, ((SCREEN_WIDTH - text_surface.get_width() + OFFSET)/2, y_offset))
            y_offset += 40

    @staticmethod
    def load_leaderboard():
        try:
            with open("leaderboard.json", 'r') as leaderboard:
                return json.load(leaderboard)
        except FileNotFoundError:
            return []