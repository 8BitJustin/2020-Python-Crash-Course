import pygame
from pygame.sprite import Sprite


class Laser(Sprite):
    """Manage lasers fired from spaceship."""
    def __init__(self, screen, bullet_length, bullet_height):
        super(Laser, self).__init__()
        self.screen

        self.rect = pygame.Rect(0,0, bullet_length, bullet_height)