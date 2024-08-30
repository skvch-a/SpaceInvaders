import unittest
import pygame
from space_invaders_game.game_objects.laser import Laser

class TestLaser(unittest.TestCase):

    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_laser_initialization(self):
        laser = Laser((100, 100), 5, (255, 0, 0))
        self.assertEqual(laser.rect.center, (100, 100))
        self.assertEqual(laser._speed, 5)
        self.assertEqual(laser.image.get_size(), (4, 15))

    def test_laser_update(self):
        laser = Laser((100, 100), 5, (255, 0, 0))
        initial_y = laser.rect.y
        laser.update()
        self.assertEqual(laser.rect.y, initial_y - 5)

    def test_laser_off_screen(self):
        laser = Laser((100, 1000), 5, (255, 0, 0))
        laser.update()
        self.assertFalse(laser.alive())

if __name__ == '__main__':
    unittest.main()
