import unittest
import pygame
from space_invaders_game.game_objects.alien_ship import AlienShip

class TestAlienShip(unittest.TestCase):

    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_alien_ship_initialization(self):
        alien = AlienShip(1, (0, 255, 0), 50, 50)
        self.assertEqual(alien.rect.topleft, (50, 50))
        self.assertEqual(alien._type, 1)

    def test_alien_ship_movement(self):
        alien = AlienShip(1, (0, 255, 0), 50, 50)
        initial_x = alien.rect.x
        alien.update(5)
        self.assertEqual(alien.rect.x, initial_x + 5)

if __name__ == '__main__':
    unittest.main()
