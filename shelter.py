from pygame.sprite import Group
from constants import OBSTACLE_GRID
from block import Block


class Shelter:
    def __init__(self, x, y):
        self.blocks_group = Group()
        self.fill_blocks_group(x, y)

    def fill_blocks_group(self, x, y):
        for row in range(len(OBSTACLE_GRID)):
            for column in range(len(OBSTACLE_GRID[0])):
                if OBSTACLE_GRID[row][column] == 1:
                    self.blocks_group.add(Block(x + column * 3, y + row * 3))
