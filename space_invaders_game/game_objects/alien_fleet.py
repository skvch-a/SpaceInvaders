from ..constants import ALIEN_FLEET_ROWS, ALIEN_FLEET_COLUMNS, GAME_AREA_WIDTH, OFFSET, ALIENS_LASER_SPEED
from .laser import Laser
from .alien_ship import AlienShip

import pygame
from random import choice

class AlienFleet(pygame.sprite.Group):
    def __init__(self, color: tuple[int, int, int]):
        """
        :param color: Цвет пришельцев и их лазеров в формате RGB
        """
        super().__init__()
        self._direction = 1
        self._lasers_group = pygame.sprite.Group()
        self._color = color
        self.create_aliens()

    def get_lasers(self) -> pygame.sprite.Group:
        return self._lasers_group

    def update_lasers(self) -> None:
        self._lasers_group.update()

    def draw_fleet_and_lasers(self, screen: pygame.Surface) -> None:
        """
        Отрисовывает флот пришельцев и их лазеры на экране.

        :param screen: Экран, на который производится отрисовка.
        """
        self.draw(screen)
        self._lasers_group.draw(screen)

    def create_aliens(self) -> None:
        """
        Создает спрайты пришельцев и добавляет их в группу
        """
        for row in range(ALIEN_FLEET_ROWS):
            for column in range(ALIEN_FLEET_COLUMNS):
                x = 75 + column * 55
                y = 110 + row * 55

                if row == 0:
                    alien_type = 3
                elif row in (1, 2):
                    alien_type = 2
                else:
                    alien_type = 1

                self.add(AlienShip(alien_type, self._color, x + OFFSET / 2, y))

    def move(self) -> None:
        """
        Перемещает пришельцев влево/вправо (в зависимости от self._direction), опускает их вниз при достижении края
        """
        self.update(self._direction)

        alien_sprites = self.sprites()
        for alien in alien_sprites:
            if alien.rect.right >= GAME_AREA_WIDTH + OFFSET / 2:
                self._direction = -1
                self.move_down()
                break
            elif alien.rect.left <= OFFSET / 2:
                self._direction = 1
                self.move_down()
                break

    def move_down(self) -> None:
        """
        Передвигает пришельцев вниз
        """
        if self:
            for alien in self.sprites():
                alien.rect.y += 15

    def shoot(self) -> None:
        """
        Случайный пришелец стреляет лазером
        """
        if self.sprites():
            random_alien = choice(self.sprites())
            self._lasers_group.add(Laser(random_alien.rect.center, ALIENS_LASER_SPEED, self._color))
