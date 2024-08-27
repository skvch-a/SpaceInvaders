import pygame
import random
from constants import SCREEN_WIDTH, OFFSET


class MysteryShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/Graphics/mystery.png")
        x, self.speed = random.choice([[OFFSET / 2, 3], [SCREEN_WIDTH + OFFSET - self.image.get_width(), -3]])
        self.rect = self.image.get_rect(topleft=(x, 90))

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > SCREEN_WIDTH + OFFSET / 2:
            self.kill()
        elif self.rect.left < OFFSET / 2:
            self.kill()
