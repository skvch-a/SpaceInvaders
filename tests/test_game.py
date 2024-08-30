import pygame
import unittest
from unittest.mock import patch

from space_invaders_game.game_core.game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.game = Game()
        self.game.start()

    def tearDown(self):
        pygame.quit()

    def test_game_over(self):
        with patch('pygame.mixer.music.stop') as mock_music_stop, \
                patch('pygame.mixer.Sound') as MockSound:
            mock_sound_instance = MockSound.return_value
            self.game.game_over()

            self.assertIsNotNone(self.game._game_over_time)
            mock_music_stop.assert_called_once()
            mock_sound_instance.play.assert_called_once()


if __name__ == '__main__':
    unittest.main()
