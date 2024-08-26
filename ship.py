import pygame
from abc import abstractmethod
from laser_gun import LaserGun

class Ship(pygame.sprite.Sprite):
    def __init__(self, path_to_image):
        super().__init__()
        self.rect = None
        self.image = pygame.image.load(path_to_image)
        self.laser_gun = LaserGun(5)

    def shoot(self):
        self.laser_gun.shoot(self.rect.center)

    @abstractmethod
    def update(self): pass


