import unittest
import pygame
from space_invaders_game.game_objects.player_ship import PlayerShip

class TestPlayerShip(unittest.TestCase):

    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_player_ship_initialization(self):
        player = PlayerShip((0, 0, 255))
        self.assertEqual(player._lives, 3)
        self.assertEqual(player.rect.midbottom, (400, 700))

    def test_player_ship_movement(self):
        player = PlayerShip((0, 0, 255))
        initial_x = player.rect.x
        player.move_right()
        self.assertGreater(player.rect.x, initial_x)
        player.move_left()
        self.assertLess(player.rect.x, initial_x + player.rect.width)

    def test_player_ship_shoot(self):
        player = PlayerShip((0, 0, 255))
        player.shoot()
        self.assertEqual(len(player.get_lasers()), 1)

if __name__ == '__main__':
    unittest.main()
