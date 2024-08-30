from .. import OBSTACLE_GRID
from .block import Block

from pygame.sprite import Group


class Shelter:
    def __init__(self, color: tuple[int, int, int], x: int, y: int):
        """
        :param color: Цвет в формате RGB
        :param x: Начальная позиция по оси X
        :param y: Начальная позиция по оси Y
        """
        self.blocks_group = Group()
        self.fill_blocks_group(color, x, y)

    def fill_blocks_group(self, color, x, y) -> None:
        for row in range(len(OBSTACLE_GRID)):
            for column in range(len(OBSTACLE_GRID[0])):
                if OBSTACLE_GRID[row][column] == 1:
                    self.blocks_group.add(Block(color, x + column * 3, y + row * 3))
