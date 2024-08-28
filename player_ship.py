import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET
from laser import Laser

class PlayerShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/Graphics/GameObjects/player_ship.png')
        self.rect = self.image.get_rect(midbottom=((SCREEN_WIDTH + OFFSET) / 2, SCREEN_HEIGHT))
        self._speed = 6
        self._shoot_delay = 300
        self._shoot_speed = 5
        self._last_shoot_time = float('-inf')
        self._lasers_group = pygame.sprite.Group()
        self._shoot_sound = pygame.mixer.Sound("Assets/Audio/shoot.ogg")

    def get_lasers(self):
        return self._lasers_group

    def update_lasers(self):
        self._lasers_group.update()

    def draw_ship_and_lasers(self, screen):
        screen.blit(self.image, self.rect)
        self._lasers_group.draw(screen)

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self._last_shoot_time >= self._shoot_delay:
            self._lasers_group.add(Laser(self.rect.center, self._shoot_speed))
            self._shoot_sound.play()
            self._last_shoot_time = pygame.time.get_ticks()

    def move_right(self):
        self.rect.x += self._speed
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_HEIGHT

    def move_left(self):
        self.rect.x -= self._speed
        if self.rect.left < OFFSET:
            self.rect.left = OFFSET
