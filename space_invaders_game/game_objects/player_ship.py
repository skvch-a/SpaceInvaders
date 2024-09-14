from ..constants import LIVES_COUNT, PLAYER_SHIP_IMAGE_PATH, SCREEN_WIDTH, GAME_AREA_HEIGHT, GET_DAMAGE_SOUND_PATH, \
    PLAYER_SHIP_SPEED, GAME_AREA_WIDTH, OFFSET, PLAYER_SHIP_SHOOT_DELAY, PLAYER_SHIP_SHOT_SPEED, SHOOT_SOUND_PATH

from ..utils.image_utils import get_image
from .laser import Laser

import pygame


class PlayerShip(pygame.sprite.Sprite):
    def __init__(self, color: tuple[int, int, int]):
        """
        :param color: Цвет корабля игрока и его лазеров в формате RGB
        """
        super().__init__()
        self._color = color
        self.image = get_image(PLAYER_SHIP_IMAGE_PATH, self._color)
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH / 2, GAME_AREA_HEIGHT))
        self._last_shoot_time = float('-inf')
        self._lasers_group = pygame.sprite.Group()
        self._shoot_sound = pygame.mixer.Sound(SHOOT_SOUND_PATH)
        self._damage_sound = pygame.mixer.Sound(GET_DAMAGE_SOUND_PATH)
        self._lives = LIVES_COUNT

    def get_lives(self) -> int:
        return self._lives

    def get_lasers(self) -> pygame.sprite.Group:
        return self._lasers_group

    def is_killed(self) -> bool:
        return self._lives <= 0

    def take_damage(self) -> None:
        self._lives -= 1
        self._damage_sound.play()

    def update_lasers(self) -> None:
        """
        Обновляет положение всех лазеров, выпущенных кораблем игрока.
        """
        self._lasers_group.update()

    def draw_ship_and_lasers(self, screen: pygame.Surface) -> None:
        """
        Отрисовывает корабль игрока и все его выпущенные лазеры на экране
        """
        screen.blit(self.image, self.rect)
        self._lasers_group.draw(screen)

    def shoot(self) -> None:
        """
        Стреляет лазером, если прошло достаточно времени с последнего выстрела
        """
        current_time = pygame.time.get_ticks()
        if current_time - self._last_shoot_time >= PLAYER_SHIP_SHOOT_DELAY:
            self._lasers_group.add(Laser(self.rect.center, PLAYER_SHIP_SHOT_SPEED, self._color))
            self._shoot_sound.play()
            self._last_shoot_time = pygame.time.get_ticks()

    def move_right(self) -> None:
        """
        Передвигает корабль игрока вправо, если это возможно
        """
        self.rect.right = min(self.rect.right + PLAYER_SHIP_SPEED, GAME_AREA_WIDTH)

    def move_left(self) -> None:
        """
        Передвигает корабль игрока влево, если это возможно
        """
        self.rect.left = max(self.rect.left - PLAYER_SHIP_SPEED, OFFSET)
