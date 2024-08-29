import pygame
from image_utils import get_image


class AlienShip(pygame.sprite.Sprite):
    def __init__(self, alien_type_number, color, x, y):
        super().__init__()
        self.image = get_image(f'Assets/Graphics/GameObjects/alien_{alien_type_number}.png', color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self._type = alien_type_number

    def get_type(self):
        return self._type

    def update(self, direction):
        self.rect.x += direction
