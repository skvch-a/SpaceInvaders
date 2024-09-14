from ..constants import GAME_AREA_WIDTH, OFFSET, GAME_AREA_HEIGHT, START_BUTTON_IMAGE_PATH, \
    MENU_BACKGROUND_IMAGE_PATH, MENU_MUSIC_PATH

from ..utils.leaderboard import draw_leaderboard

import pygame


class Menu:
    def __init__(self):
        self.background_img = pygame.image.load(MENU_BACKGROUND_IMAGE_PATH)
        self.background_rect = self.background_img.get_rect()

        self.play_button_img = pygame.image.load(START_BUTTON_IMAGE_PATH)
        self.play_button_rect = self.play_button_img.get_rect(center=((GAME_AREA_WIDTH + OFFSET) / 2, GAME_AREA_HEIGHT / 2))

    @staticmethod
    def start_music() -> None:
        pygame.mixer.music.load(MENU_MUSIC_PATH)
        pygame.mixer.music.play(-1)

    def draw(self, screen) -> None:
        screen.blit(self.background_img, self.background_rect)
        screen.blit(self.play_button_img, self.play_button_rect)
        draw_leaderboard(screen)
