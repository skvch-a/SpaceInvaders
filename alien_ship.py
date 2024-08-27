import pygame


class AlienShip(pygame.sprite.Sprite):
    def __init__(self, alien_type_number, x, y):
        super().__init__()
        self.image = pygame.image.load(f'Assets/Graphics/alien_{alien_type_number}.png')
        self.type = alien_type_number
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direction):
        self.rect.x += direction
