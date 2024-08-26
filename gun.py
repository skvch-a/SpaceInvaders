import pygame
from laser import Laser

class Gun:
    def __init__(self, lasers_group):
        self.lasers_group = lasers_group
        self.shoot_delay = 300
        self.last_shoot_time = float('-inf')
        self.shoot_sound = pygame.mixer.Sound("Assets/Audio/shoot.ogg")

    def shoot(self, laser):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shoot_time >= self.shoot_delay:
            self.lasers_group.add(laser)
            self.shoot_sound.play()
            self.last_shoot_time = pygame.time.get_ticks()