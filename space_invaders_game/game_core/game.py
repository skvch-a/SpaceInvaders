from ..constants import LEVEL_UP_SCORE, BASIC_ALIEN_SCORE, GAME_MUSIC_PATH, START_FPS, EXPLOSION_SOUND_PATH, \
    GAME_MUSIC_VOLUME, GAME_OVER_SOUND_PATH, LEVEL_COLORS, LEVEL_UP_SOUND_PATH, MYSTERY_SHIP_SCORE, OBSTACLE_GRID, \
    GAME_AREA_WIDTH, OFFSET, GAME_AREA_HEIGHT, SHELTERS_OFFSET_Y

from .game_message_screen import GameMessageScreen
from ..utils.leaderboard import update_leaderboard, get_max_score
from ..game_objects.alien_fleet import AlienFleet
from ..game_objects.player_ship import PlayerShip
from ..game_objects.mystery_ship import MysteryShip
from ..game_objects.shelter import Shelter

import pygame
from time import time


class Game:
    def __init__(self):
        self._run = False
        self._on_pause = False
        self._FPS = None
        self._level_number = None
        self._level_color = None
        self._player_ship = None
        self._shelters = None
        self._alien_fleet = None
        self._mystery_ship_group = None
        self._score = None
        self._highscore = None
        self._explosion_sound = None
        self._level_up_sound = None
        self._game_over_time = None
        self._game_over_screen = None
        self._pause_screen = None

    def start(self) -> None:
        """Запускает игру, инициализируя игровые объекты"""
        self._run = True
        self._on_pause = False
        self._FPS = START_FPS
        self._level_number = 1
        self._level_color = self.get_level_color()
        self._player_ship = PlayerShip(self._level_color)
        self._shelters = self.create_shelters()
        self._alien_fleet = AlienFleet(self._level_color)
        self._mystery_ship_group = pygame.sprite.GroupSingle()
        self._score = 0
        self._highscore = get_max_score()
        self._explosion_sound = pygame.mixer.Sound(EXPLOSION_SOUND_PATH)
        self._level_up_sound = pygame.mixer.Sound(LEVEL_UP_SOUND_PATH)
        self._game_over_time = None
        self._game_over_screen = None
        self._pause_screen = None
        pygame.mixer.music.load(GAME_MUSIC_PATH)
        pygame.mixer.music.set_volume(GAME_MUSIC_VOLUME)
        pygame.mixer.music.play(-1)

    def stop(self) -> None:
        """Останавливает игру, обновляет таблицу лидеров"""
        pygame.mixer.music.stop()
        self._run = False
        update_leaderboard(self._score, self._level_number)

    def pause(self) -> None:
        """Ставит игру на паузу"""
        pygame.mixer.music.pause()
        self._pause_screen = GameMessageScreen(self._level_color, "PAUSE")
        self._on_pause = True

    def resume(self) -> None:
        """Снимает игру с паузы"""
        pygame.mixer.music.unpause()
        self._on_pause = False

    def is_paused(self) -> bool:
        return self._on_pause

    def game_over(self) -> None:
        """Завершает игру и проигрывает звук окончания игры"""
        pygame.mixer.music.stop()
        self._game_over_time = time()
        self._game_over_screen = GameMessageScreen(self._level_color, "GAME OVER!")
        game_over_sound = pygame.mixer.Sound(GAME_OVER_SOUND_PATH)
        game_over_sound.play()

    def level_up(self) -> None:
        """Переход на следующий уровень"""
        self._level_up_sound.play()
        self._score += LEVEL_UP_SCORE
        self._level_number += 1
        self._FPS += 10
        self._level_color = self.get_level_color()
        self._player_ship = PlayerShip(self._level_color)
        self._shelters = self.create_shelters()
        self._alien_fleet = AlienFleet(self._level_color)
        self._mystery_ship_group = pygame.sprite.GroupSingle()

    def get_fps(self) -> int:
        return self._FPS

    def get_level_number(self) -> int:
        return self._level_number

    def get_level_color(self) -> tuple[int, int, int]:
        return LEVEL_COLORS[(self._level_number - 1) % len(LEVEL_COLORS)]

    def is_running(self) -> bool:
        return self._run

    def get_score(self) -> int:
        return self._score

    def get_player_ship(self) -> PlayerShip:
        return self._player_ship

    def alien_fleet_shoot(self) -> None:
        self._alien_fleet.shoot()

    def draw_game_objects(self, screen: pygame.Surface) -> None:
        """Рисует игровые объекты на экране"""
        if self._game_over_screen:
            self._game_over_screen.draw(screen)
        elif self._on_pause:
            self._pause_screen.draw(screen)
        else:
            self._player_ship.draw_ship_and_lasers(screen)
            for obstacle in self._shelters:
                obstacle.blocks_group.draw(screen)
            self._alien_fleet.draw_fleet_and_lasers(screen)
            self._mystery_ship_group.draw(screen)

    def update(self) -> None:
        """Обновляет игровые объекты, проверяет условия завершения игры или перехода на следующий уровень"""
        if self._game_over_time:
            if time() - self._game_over_time > 3:
                self.stop()
        else:
            if len(self._alien_fleet) == 0:
                self.level_up()
            else:
                self._alien_fleet.move()
                self._alien_fleet.update_lasers()
                self._player_ship.update_lasers()
                self._mystery_ship_group.update()
                self.check_for_collisions()

    def launch_mystery_ship(self) -> None:
        self._mystery_ship_group.add(MysteryShip(self._level_color))

    def check_player_ship_lasers_collisions(self) -> None:
        """Проверяет столкновения лазеров игрока с другими объектами"""
        if self._player_ship.get_lasers():
            for laser_sprite in self._player_ship.get_lasers():
                aliens_hit = pygame.sprite.spritecollide(laser_sprite, self._alien_fleet, True)
                if aliens_hit:
                    self._explosion_sound.play()
                    for alien in aliens_hit:
                        self._score += alien.get_type() * BASIC_ALIEN_SCORE
                        laser_sprite.kill()

                if pygame.sprite.spritecollide(laser_sprite, self._mystery_ship_group, True):
                    self._score += MYSTERY_SHIP_SCORE
                    self._explosion_sound.play()
                    laser_sprite.kill()

                for obstacle in self._shelters:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

    def check_alien_fleet_lasers_collisions(self) -> None:
        """Проверяет столкновения лазеров пришельцев с другими объектами."""
        if self._alien_fleet.get_lasers():
            for laser_sprite in self._alien_fleet.get_lasers():
                if pygame.sprite.collide_rect(laser_sprite, self._player_ship):
                    laser_sprite.kill()
                    self._player_ship.take_damage()
                    if self._player_ship.is_killed():
                        self.game_over()

                for obstacle in self._shelters:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

    def check_for_collisions(self) -> None:
        """Проверяет все столкновения"""
        self.check_player_ship_lasers_collisions()
        self.check_alien_fleet_lasers_collisions()
        if self._alien_fleet:
            for alien in self._alien_fleet:
                for obstacle in self._shelters:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)

                if pygame.sprite.collide_rect(alien, self._player_ship) or alien.rect.y >= GAME_AREA_HEIGHT:
                    self.game_over()

    def create_shelters(self) -> list[Shelter]:
        shelter_width = len(OBSTACLE_GRID[0]) * 3
        gap = (GAME_AREA_WIDTH + OFFSET - (4 * shelter_width)) / 5
        shelters = []
        for i in range(4):
            pos_x = (i + 1) * gap + i * shelter_width
            shelter = Shelter(self._level_color, pos_x, GAME_AREA_HEIGHT - SHELTERS_OFFSET_Y)
            shelters.append(shelter)
        return shelters
