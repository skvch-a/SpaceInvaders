from .. import ALIEN_SPEED
from ..utils.image_utils import get_image

import pygame


class AlienShip(pygame.sprite.Sprite):
    def __init__(self, alien_type_number: int, color: tuple[int, int, int], x: int, y: int):
        """
        :param alien_type_number: Тип корабля пришельца
        :param color: Цвет корабля в формате RGB
        :param x: Начальная позиция корабля по оси X
        :param y: Начальная позиция корабля по оси Y
        """
        super().__init__()
        self.image = get_image(f'space_invaders_game/assets/graphics/game_objects/alien_{alien_type_number}.png', color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self._type = alien_type_number

    def get_type(self) -> int:
        return self._type

    def update(self, direction: int) -> None:
        """
        Обновляет позицию корабля по оси X в зависимости от direction
        """
        self.rect.x += direction * ALIEN_SPEED
