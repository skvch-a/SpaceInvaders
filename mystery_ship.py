import pygame
import random
from constants import SCREEN_WIDTH, OFFSET
from image_utils import get_image


class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = get_image("Assets/Graphics/GameObjects/mystery.png", color)
        rect_x, self._speed = random.choice([[OFFSET / 2, 3], [SCREEN_WIDTH + OFFSET - self.image.get_width(), -3]])
        self.rect = self.image.get_rect(topleft=(rect_x, 90))

    def update(self):
        self.rect.x += self._speed
        if self.rect.right > SCREEN_WIDTH + OFFSET / 2:
            self.kill()
        elif self.rect.left < OFFSET / 2:
            self.kill()
