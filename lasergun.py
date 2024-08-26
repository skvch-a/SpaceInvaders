import pygame
from laser import Laser

class LaserGun:
    def __init__(self, screen_height, shoot_speed):
        self.screen_height = screen_height
        self.shoot_speed = shoot_speed
        self.lasers_group = pygame.sprite.Group()
        self.shoot_delay = 300
        self.last_shoot_time = float('-inf')
        self.shoot_sound = pygame.mixer.Sound("Assets/Audio/shoot.ogg")

    def update(self):
        self.lasers_group.update()

    def shoot(self, position):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shoot_time >= self.shoot_delay:
            self.lasers_group.add(Laser(position, self.shoot_speed, self.screen_height))
            self.shoot_sound.play()
            self.last_shoot_time = pygame.time.get_ticks()