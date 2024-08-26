from constants import SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET
from ship import Ship


class PlayerShip(Ship):
	def __init__(self):
		super().__init__("Assets/Graphics/playership.png")
		self.rect = self.image.get_rect(midbottom = ((SCREEN_WIDTH + OFFSET) / 2, SCREEN_HEIGHT))
		self.speed = 6

	def update(self):
		self.laser_gun.update()

	def move_right(self):
		self.rect.x += self.speed
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_HEIGHT

	def move_left(self):
		self.rect.x -= self.speed
		if self.rect.left < OFFSET:
			self.rect.left = OFFSET


