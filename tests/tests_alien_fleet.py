import unittest
import pygame

from space_invaders_game.constants import *
from space_invaders_game.game_objects.alien_fleet import AlienFleet
from space_invaders_game.game_objects.alien_ship import AlienShip
from space_invaders_game.game_objects.laser import Laser

class TestAlienFleet(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.color = (255, 0, 0)
        self.fleet = AlienFleet(self.color)

    def tearDown(self):
        pygame.quit()

    def test_create_aliens(self):
        self.assertEqual(len(self.fleet.sprites()), ALIEN_FLEET_ROWS * ALIEN_FLEET_COLUMNS)
        for alien in self.fleet.sprites():
            self.assertIsInstance(alien, AlienShip)

    def test_move(self):
        initial_positions = [alien.rect.topleft for alien in self.fleet.sprites()]
        self.fleet.move()

        moved_positions = [alien.rect.topleft for alien in self.fleet.sprites()]
        self.assertNotEqual(initial_positions, moved_positions)

    def test_shoot(self):
        initial_laser_count = len(self.fleet.get_lasers().sprites())
        self.fleet.shoot()
        new_laser_count = len(self.fleet.get_lasers().sprites())
        self.assertEqual(new_laser_count, initial_laser_count + 1)
        self.assertIsInstance(self.fleet.get_lasers().sprites()[0], Laser)

    def test_update_lasers(self):
        self.fleet.shoot()
        lasers = self.fleet.get_lasers().sprites()
        initial_y_positions = [laser.rect.y for laser in lasers]

        self.fleet.update_lasers()

        updated_y_positions = [laser.rect.y for laser in lasers]
        self.assertNotEqual(initial_y_positions, updated_y_positions)

    def test_move_down(self):
        initial_y_positions = [alien.rect.y for alien in self.fleet.sprites()]
        self.fleet.move_down()
        new_y_positions = [alien.rect.y for alien in self.fleet.sprites()]

        for initial_y, new_y in zip(initial_y_positions, new_y_positions):
            self.assertEqual(new_y, initial_y + ALIENS_MOVE_DOWN_SPEED)


if __name__ == '__main__':
    unittest.main()
