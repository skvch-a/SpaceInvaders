import pygame
from constants import OBSTACLE_GRID
from block import Block


class Obstacle:
	def __init__(self, x, y):
		self.blocks_group = pygame.sprite.Group()
		for row in range(len(OBSTACLE_GRID)):
			for column in range(len(OBSTACLE_GRID[0])):
				if OBSTACLE_GRID[row][column] == 1:
					self.blocks_group.add(Block(x + column * 3, y + row * 3))

