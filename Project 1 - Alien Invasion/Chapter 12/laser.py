import pygame
from pygame.sprite import Sprite


class Laser(Sprite):
    """Manage lasers fired from spaceship."""
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.laser_width,
                                settings.laser_height)

        self.rect.left = self.rect.left
        self.rect.centery = self.rect.centery

        self.y = float(self.rect.y)

        self.color = settings.laser_color
        self.speed_factor = settings.laser_speed_factor

    def update(self):
        self.y += self.speed_factor

        self.rect.x = self.y

    def draw_laser(self):
        pygame.draw.rect(self.screen, self.color, self.rect)