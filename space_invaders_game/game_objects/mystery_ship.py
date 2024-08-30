import random

import pygame

from .. import OFFSET, MYSTERY_SHIP_IMAGE_PATH, SCREEN_WIDTH, GAME_AREA_WIDTH, MYSTERY_SHIP_SPEED
from ..utils.image_utils import get_image


class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, color: tuple[int, int, int]):
        super().__init__()
        self.image = get_image(MYSTERY_SHIP_IMAGE_PATH, color)
        rect_x, self._speed = random.choice([[OFFSET / 2, MYSTERY_SHIP_SPEED],
                                             [SCREEN_WIDTH - self.image.get_width(), -1 * MYSTERY_SHIP_SPEED]])
        self.rect = self.image.get_rect(topleft=(rect_x, 90))

    def update(self) -> None:
        self.rect.x += self._speed
        if self.rect.right > GAME_AREA_WIDTH + OFFSET / 2:
            self.kill()
        elif self.rect.left < OFFSET / 2:
            self.kill()
