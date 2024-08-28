import pygame

class AlienShip(pygame.sprite.Sprite):
    def __init__(self, alien_type_number, x, y):
        super().__init__()
        self.image = pygame.image.load(f'Assets/Graphics/GameObjects/alien_{alien_type_number}.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        self._type = alien_type_number

    def get_type(self):
        return self._type

    def update(self, direction):
        self.rect.x += direction
