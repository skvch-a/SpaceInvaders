import pygame

class AlienShip(pygame.sprite.Sprite):
	def __init__(self, type, x, y):
		super().__init__()
		self.type = type
		self.image = pygame.image.load(f"Assets/Graphics/alien_{type}.png")
		self.rect = self.image.get_rect(topleft = (x, y))

	def update(self, direction):
		self.rect.x += direction