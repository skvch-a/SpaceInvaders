import pygame
from constants import *
from leaderboard import get_max_score


class Renderer:
    def __init__(self, game, menu):
        self.game = game
        self.menu = menu
        self.screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + OFFSET * 2))

    def draw_frame(self):
        pygame.draw.rect(self.screen, GREEN, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
        pygame.draw.line(self.screen, GREEN, (25, 730), (775, 730), 3)

    def draw_text(self):
        font = pygame.font.Font("Assets/Font/monogram.ttf", FONT_SIZE)
        level_surface = font.render("LEVEL 01", False, GREEN)
        game_over_surface = font.render("GAME OVER", False, GREEN)
        score_text_surface = font.render("SCORE", False, GREEN)
        highscore_text_surface = font.render("HIGH-SCORE", False, GREEN)

        if self.game.is_running():
            self.screen.blit(level_surface, (570, 740, 50, 50))
        else:
            self.screen.blit(game_over_surface, (570, 740, 50, 50))

        x = 50
        for life in range(self.game.get_lives()):
            self.screen.blit(self.game.get_player_ship_image(), (x, 745))
            x += 50

        self.screen.blit(score_text_surface, (50, 15, 50, 50))
        formatted_score = str(self.game.get_score()).zfill(5)
        score_surface = font.render(formatted_score, False, GREEN)
        self.screen.blit(score_surface, (50, 40, 50, 50))
        self.screen.blit(highscore_text_surface, (550, 15, 50, 50))
        formatted_highscore = str(get_max_score()).zfill(5)
        highscore_surface = font.render(formatted_highscore, False, GREEN)
        self.screen.blit(highscore_surface, (625, 40, 50, 50))

    def draw_game_objects(self):
        self.game.draw_player_ship_and_lasers(self.screen)
        self.game.draw_obstacles(self.screen)
        self.game.draw_alien_fleet_and_lasers(self.screen)
        self.game.draw_mystery_ship(self.screen)

    def render(self):
        if self.game.is_running():
            self.render_game()
        else:
            self.render_menu()

    def render_menu(self):
        self.menu.draw(self.screen)

    def render_game(self):
        self.screen.fill(GREY)
        self.draw_frame()
        self.draw_text()
        self.draw_game_objects()