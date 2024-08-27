import pygame
from constants import *

class Visualizer:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + OFFSET * 2))

    def draw_frame(self):
        pygame.draw.rect(self.screen, YELLOW, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
        pygame.draw.line(self.screen, YELLOW, (25, 730), (775, 730), 3)

    def draw_text(self):
        font = pygame.font.Font("Assets/Font/monogram.ttf", FONT_SIZE)
        level_surface = font.render("LEVEL 01", False, YELLOW)
        game_over_surface = font.render("GAME OVER", False, YELLOW)
        score_text_surface = font.render("SCORE", False, YELLOW)
        highscore_text_surface = font.render("HIGH-SCORE", False, YELLOW)

        if self.game.run:
            self.screen.blit(level_surface, (570, 740, 50, 50))
        else:
            self.screen.blit(game_over_surface, (570, 740, 50, 50))

        x = 50
        for life in range(self.game.lives):
            self.screen.blit(self.game.player_ship.image, (x, 745))
            x += 50

        self.screen.blit(score_text_surface, (50, 15, 50, 50))
        formatted_score = str(self.game.score).zfill(5)
        score_surface = font.render(formatted_score, False, YELLOW)
        self.screen.blit(score_surface, (50, 40, 50, 50))
        self.screen.blit(highscore_text_surface, (550, 15, 50, 50))
        formatted_highscore = str(self.game.highscore).zfill(5)
        highscore_surface = font.render(formatted_highscore, False, YELLOW)
        self.screen.blit(highscore_surface, (625, 40, 50, 50))

    def draw_game_objects(self):
        self.screen.blit(self.game.player_ship.image, self.game.player_ship.rect)
        self.game.player_ship.lasers_group.draw(self.screen)
        for obstacle in self.game.obstacles:
            obstacle.blocks_group.draw(self.screen)
        self.game.alien_fleet.draw(self.screen)
        self.game.alien_fleet.lasers_group.draw(self.screen)
        self.game.mystery_ship_group.draw(self.screen)

    def visualize(self):
        self.screen.fill(GREY)
        self.draw_frame()
        self.draw_text()
        self.draw_game_objects()