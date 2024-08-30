import pygame

def get_image(path, color):

    image = pygame.image.load(path)
    image.fill((0, 0, 0, 255), special_flags=pygame.BLEND_RGBA_MULT)
    image.fill(color[0:3] + (0,), special_flags=pygame.BLEND_RGBA_ADD)
    return image

