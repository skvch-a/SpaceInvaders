import pygame
from constants import GAME_AREA_HEIGHT, LASER_WIDTH, LASER_HEIGHT


class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, color):
        super().__init__()
        self.image = pygame.Surface((LASER_WIDTH, LASER_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=position)
        self._speed = speed

    def update(self):
        self.rect.y -= self._speed
        if self.rect.y > GAME_AREA_HEIGHT + 15 or self.rect.y < 0:
            self.kill()
