import pygame
from laser import Laser
from gun import Gun


class PlayerShip(pygame.sprite.Sprite):
	def __init__(self, screen_width, screen_height, offset):
		super().__init__()
		self.offset = offset
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.image = pygame.image.load("Assets/Graphics/playership.png")
		self.rect = self.image.get_rect(midbottom = ((self.screen_width + self.offset)/2, self.screen_height))
		self.speed = 6
		self.lasers_group = pygame.sprite.Group()
		self.gun = Gun(self.lasers_group)


	def update(self):
		self.process_user_input()
		self.lasers_group.update()

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
			self.gun.shoot(Laser(self.rect.center, 5, self.screen_height))

	def reset(self):
		self.rect = self.image.get_rect(midbottom=((self.screen_width + self.offset) / 2, self.screen_height))
		self.lasers_group.empty()