import pygame
import unittest
from unittest.mock import patch, MagicMock

from space_invaders_game.game_core.event_handler import EventHandler


class TestEventHandler(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.mock_game = MagicMock()
        self.mock_menu = MagicMock()
        self.event_handler = EventHandler(self.mock_game, self.mock_menu)

    def tearDown(self):
        pygame.quit()

    @patch('pygame.event.get')
    def test_handle_events_quit(self, mock_event_get):
        mock_event_get.return_value = [pygame.event.Event(pygame.QUIT)]

        with self.assertRaises(SystemExit):
            self.event_handler.handle_events()

    @patch('pygame.event.get')
    @patch('pygame.mixer.music.get_busy', return_value=False)
    def test_handle_events_menu_music(self, mock_music_busy, mock_event_get):
        mock_event_get.return_value = []
        self.mock_game.is_running.return_value = False

        self.event_handler.handle_events()
        self.mock_menu.start_music.assert_called_once()

    @patch('pygame.event.get')
    def test_handle_events_game_running(self, mock_event_get):
        mock_event_get.return_value = [
            pygame.event.Event(self.event_handler.shoot_laser_event),
            pygame.event.Event(self.event_handler.mystery_ship_event)
        ]
        self.mock_game.is_running.return_value = True
        self.mock_game.is_paused.return_value = False
        self.event_handler.handle_events()
        self.mock_game.alien_fleet_shoot.assert_called_once()
        self.mock_game.launch_mystery_ship.assert_called_once()

    @patch('pygame.event.get')
    def test_handle_events_escape_key(self, mock_event_get):
        mock_event_get.return_value = [pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_ESCAPE})]
        self.mock_game.is_paused.return_value = False
        self.event_handler.handle_events()
        self.mock_game.pause.assert_called_once()

    @patch('pygame.event.get')
    def test_handle_events_start_game(self, mock_event_get):
        mock_event_get.return_value = [pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': (50, 50)})]
        self.mock_game.is_running.return_value = False
        self.mock_menu.play_button_rect.collidepoint.return_value = True
        self.event_handler.handle_events()
        self.mock_game.start.assert_called_once()

    @patch('pygame.key.get_pressed')
    def test_handle_player_controls(self, mock_get_pressed):
        mock_get_pressed.return_value = {
            pygame.K_RIGHT: True,
            pygame.K_LEFT: False,
            pygame.K_SPACE: False
        }
        mock_player_ship = MagicMock()
        self.mock_game.get_player_ship.return_value = mock_player_ship
        self.event_handler.handle_player_controls()
        mock_player_ship.move_right.assert_called_once()
        mock_player_ship.move_left.assert_not_called()
        mock_player_ship.shoot.assert_not_called()

    @patch('pygame.key.get_pressed')
    def test_handle_player_controls_shoot(self, mock_get_pressed):
        mock_get_pressed.return_value = {
            pygame.K_RIGHT: False,
            pygame.K_LEFT: False,
            pygame.K_SPACE: True
        }
        mock_player_ship = MagicMock()
        self.mock_game.get_player_ship.return_value = mock_player_ship
        self.event_handler.handle_player_controls()
        mock_player_ship.shoot.assert_called_once()

    def test_update_game_objects(self):
        with patch.object(self.event_handler, 'handle_player_controls') as mock_handle_player_controls, \
             patch.object(self.mock_game, 'update') as mock_game_update:
            self.event_handler.update_game_objects()
            mock_handle_player_controls.assert_called_once()
            mock_game_update.assert_called_once()


if __name__ == '__main__':
    unittest.main()
