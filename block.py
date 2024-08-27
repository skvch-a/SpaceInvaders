import pygame
from constants import GREEN

class Block(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface((3,3))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect(topleft = (x,y))