import pygame
from constants import *
from image_utils import get_image
from laser import Laser

class PlayerShip(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self._color = color
        self.image = get_image(PLAYER_SHIP_IMAGE_PATH, self._color)
        self.rect = self.image.get_rect(midbottom=((SCREEN_WIDTH + OFFSET) / 2, SCREEN_HEIGHT))
        self._last_shoot_time = float('-inf')
        self._lasers_group = pygame.sprite.Group()
        self._shoot_sound = pygame.mixer.Sound(SHOOT_SOUND_PATH)

    def get_lasers(self):
        return self._lasers_group

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
        self.rect.right = min(self.rect.right + PLAYER_SHIP_SPEED, SCREEN_WIDTH)

    def move_left(self):
        self.rect.left = max(self.rect.left - PLAYER_SHIP_SPEED, OFFSET)
