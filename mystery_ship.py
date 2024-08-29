import pygame
import random
from constants import OFFSET, MYSTERY_SHIP_IMAGE_PATH, SCREEN_WIDTH, GAME_AREA_WIDTH
from image_utils import get_image


class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = get_image(MYSTERY_SHIP_IMAGE_PATH, color)
        rect_x, self._speed = random.choice([[OFFSET / 2, 3], [SCREEN_WIDTH - self.image.get_width(), -3]])
        self.rect = self.image.get_rect(topleft=(rect_x, 90))

    def update(self):
        self.rect.x += self._speed
        if self.rect.right > GAME_AREA_WIDTH + OFFSET / 2:
            self.kill()
        elif self.rect.left < OFFSET / 2:
            self.kill()
