import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, color: tuple[int, int, int], x: int, y: int):
        """
        :param color: Цвет в формате RGB
        :param x: Начальная позиция по оси X
        :param y: Начальная позиция по оси Y
        """
        super().__init__()
        self.image = pygame.Surface((3, 3))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
