import pygame
from constants import SCREEN_HEIGHT, LASER_WIDTH, LASER_HEIGHT


class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, color):
        super().__init__()
        self.image = pygame.Surface((LASER_WIDTH, LASER_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=position)
        self._speed = speed

    def update(self):
        self.rect.y -= self._speed
        if self.rect.y > SCREEN_HEIGHT + 15 or self.rect.y < 0:
            self.kill()
