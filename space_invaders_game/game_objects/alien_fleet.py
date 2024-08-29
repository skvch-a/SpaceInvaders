from .. import *
from .laser import Laser
from .alien_ship import AlienShip

from pygame.sprite import Group
from random import choice

class AlienFleet(Group):
    def __init__(self, color):
        super().__init__()
        self._direction = 1
        self._lasers_group = Group()
        self._color = color
        self.create_aliens()

    def get_lasers(self):
        return self._lasers_group

    def update_lasers(self):
        self._lasers_group.update()

    def draw_fleet_and_lasers(self, screen):
        self.draw(screen)
        self._lasers_group.draw(screen)

    def create_aliens(self):
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

    def move(self):
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

    def move_down(self):
        if self:
            for alien in self.sprites():
                alien.rect.y += ALIENS_MOVE_DOWN_SPEED

    def shoot(self):
        if self.sprites():
            random_alien = choice(self.sprites())
            self._lasers_group.add(Laser(random_alien.rect.center, ALIENS_LASER_SPEED, self._color))
