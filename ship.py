import pygame
from abc import abstractmethod
from lasergun import LaserGun

class Ship(pygame.sprite.Sprite):
    def __init__(self, screen_height, path_to_image):
        super().__init__()
        self.rect = None
        self.image = pygame.image.load(path_to_image)
        self.gun = LaserGun(screen_height, 5)

    def shoot(self):
        self.gun.shoot(self.rect.center)

    @abstractmethod
    def update(self): pass


