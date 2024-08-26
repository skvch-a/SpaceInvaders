import pygame
from laser import Laser

class AlienShip(pygame.sprite.Sprite):
	def __init__(self, alien_type_number, x, y, alien_lasers_group):
		super().__init__()
		self.image = pygame.image.load(f'Assets/Graphics/alien_{alien_type_number}.png')
		self.type = alien_type_number
		self.rect = self.image.get_rect(topleft = (x, y))
		self.lasers_group = alien_lasers_group

	def update(self, direction):
		self.rect.x += direction

	def shoot(self):
		self.lasers_group.add(Laser(self.rect.center, -6))
