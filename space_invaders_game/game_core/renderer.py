from ..constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_PATH, GAME_INTERFACE_FONT_SIZE, GREY
from ..utils.leaderboard import get_max_score

import pygame


class Renderer:
    def __init__(self, game, menu):
        self._game = game
        self._menu = menu
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_frame(self) -> None:
        """
        Отрисовывает рамку и разделительную линию на игровом экране
        """
        pygame.draw.rect(self._screen, self._game.get_level_color(), (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
        pygame.draw.line(self._screen, self._game.get_level_color(), (12, 730), (788, 730), 3)

    def draw_text(self) -> None:
        """
        Отображает на экране информацию об уровне, количестве жизней, текущем и максимальном счетах
        """
        font = pygame.font.Font(FONT_PATH, GAME_INTERFACE_FONT_SIZE)
        color = self._game.get_level_color()

        level_surface = font.render(f"LEVEL {self._game.get_level_number():02}", False, color)
        self._screen.blit(level_surface, (570, 740, 50, 50))

        x = 50
        for life in range(self._game.get_player_ship().get_lives()):
            self._screen.blit(self._game.get_player_ship().image, (x, 745))
            x += 50

        score_text_surface = font.render("SCORE", False, color)
        score_surface = font.render(str(self._game.get_score()).zfill(5), False, color)
        self._screen.blit(score_text_surface, (50, 15, 50, 50))
        self._screen.blit(score_surface, (50, 40, 50, 50))

        highscore_text_surface = font.render("HIGH-SCORE", False, color)
        highscore_surface = font.render(str(get_max_score()).zfill(5), False, color)
        self._screen.blit(highscore_text_surface, (550, 15, 50, 50))
        self._screen.blit(highscore_surface, (625, 40, 50, 50))

    def render(self) -> None:
        """
        Отрисовывает либо игровой процесс, либо меню в зависимости от состояния игры
        """
        if self._game.is_running():
            self.render_game()
        else:
            self.render_menu()

    def render_menu(self) -> None:
        """
        Отрисовывает меню
        """
        self._menu.draw(self._screen)

    def render_game(self) -> None:
        """
        Отрисовывает кадр игры, включая фон, рамку, текстовую информацию и игровые объекты
        """
        self._screen.fill(GREY)
        self.draw_frame()
        self.draw_text()
        self._game.draw_game_objects(self._screen)
