import pygame
from ship import Ship


class PlayerShip(Ship):
	def __init__(self, screen_width, screen_height, offset):
		super().__init__(screen_height, "Assets/Graphics/playership.png")
		self.offset = offset
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.rect = self.image.get_rect(midbottom = ((self.screen_width + self.offset) / 2, self.screen_height))
		self.speed = 6

	def update(self):
		self.process_user_input()
		self.gun.update()

	def process_user_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.rect.x += self.speed
			if self.rect.right > self.screen_width:
				self.rect.right = self.screen_width
		if keys[pygame.K_LEFT]:
			self.rect.x -= self.speed
			if self.rect.left < self.offset:
				self.rect.left = self.offset

		if keys[pygame.K_SPACE]:
			self.shoot()

