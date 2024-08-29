from .. import *
from ..utils.image_utils import get_image
from .laser import Laser

import pygame


class PlayerShip(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self._color = color
        self.image = get_image(PLAYER_SHIP_IMAGE_PATH, self._color)
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH / 2, GAME_AREA_HEIGHT))
        self._last_shoot_time = float('-inf')
        self._lasers_group = pygame.sprite.Group()
        self._shoot_sound = pygame.mixer.Sound(SHOOT_SOUND_PATH)
        self._damage_sound = pygame.mixer.Sound(GET_DAMAGE_SOUND_PATH)
        self._lives = LIVES_COUNT

    def get_lives(self):
        return self._lives

    def get_lasers(self):
        return self._lasers_group

    def is_killed(self):
        return self._lives <= 0

    def take_damage(self):
        self._lives -= 1
        self._damage_sound.play()

    def update_lasers(self):
        self._lasers_group.update()

    def draw_ship_and_lasers(self, screen):
        screen.blit(self.image, self.rect)
        self._lasers_group.draw(screen)

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self._last_shoot_time >= PLAYER_SHIP_SHOOT_DELAY:
            self._lasers_group.add(Laser(self.rect.center, PLAYER_SHIP_SHOT_SPEED, self._color))
            self._shoot_sound.play()
            self._last_shoot_time = pygame.time.get_ticks()

    def move_right(self):
        self.rect.right = min(self.rect.right + PLAYER_SHIP_SPEED, GAME_AREA_WIDTH)

    def move_left(self):
        self.rect.left = max(self.rect.left - PLAYER_SHIP_SPEED, OFFSET)
