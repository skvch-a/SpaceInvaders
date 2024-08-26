import pygame
from constants import SCREEN_HEIGHT

class Laser(pygame.sprite.Sprite):
	def __init__(self, position, speed):
		super().__init__()
		self.image = pygame.Surface((4,15))
		self.image.fill((243, 216, 63))
		self.rect = self.image.get_rect(center = position)
		self.speed = speed

	def update(self):
		self.rect.y -= self.speed
		if self.rect.y > SCREEN_HEIGHT + 15 or self.rect.y < 0:
			self.kill()
