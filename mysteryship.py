import pygame, random

class MysteryShip(pygame.sprite.Sprite):
	def __init__(self, screen_width, offset):
		super().__init__()
		self.screen_width = screen_width
		self.offset = offset
		self.image = pygame.image.load("Assets/Graphics/mystery.png")

		x = random.choice([self.offset/2, self.screen_width + self.offset - self.image.get_width()])
		if x == self.offset/2:
			self.speed = 3
		else:
			self.speed = -3

		self.rect = self.image.get_rect(topleft = (x, 90))

	def update(self):
		self.rect.x += self.speed
		if self.rect.right > self.screen_width + self.offset / 2:
			self.kill()
		elif self.rect.left < self.offset/2:
			self.kill()