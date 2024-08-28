from pygame.sprite import Group
from constants import SCREEN_WIDTH, OFFSET
from random import choice
from laser import Laser
from alien_ship import AlienShip

class AlienFleet(Group):
    def __init__(self):
        super().__init__()
        self._direction = 1
        self._lasers_group = Group()
        self.create_aliens()

    def get_lasers(self):
        return self._lasers_group

    def update_lasers(self):
        self._lasers_group.update()

    def draw_fleet_and_lasers(self, screen):
        self.draw(screen)
        self._lasers_group.draw(screen)

    def create_aliens(self):
        for row in range(5):
            for column in range(11):
                x = 75 + column * 55
                y = 110 + row * 55

                if row == 0:
                    alien_type = 3
                elif row in (1, 2):
                    alien_type = 2
                else:
                    alien_type = 1

                alien = AlienShip(alien_type, x + OFFSET / 2, y)
                self.add(alien)

    def move(self):
        self.update(self._direction)

        alien_sprites = self.sprites()
        for alien in alien_sprites:
            if alien.rect.right >= SCREEN_WIDTH + OFFSET / 2:
                self._direction = -1
                self.move_down(2)
            elif alien.rect.left <= OFFSET / 2:
                self._direction = 1
                self.move_down(2)

    def move_down(self, distance):
        if self:
            for alien in self.sprites():
                alien.rect.y += distance

    def shoot(self):
        if self.sprites():
            random_alien = choice(self.sprites())
            self._lasers_group.add(Laser(random_alien.rect.center, -6))
