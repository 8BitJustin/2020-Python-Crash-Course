import pygame
from pygame.sprite import Sprite


class Laser(Sprite):
    """Manage lasers fired from spaceship."""
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.laser_width,
                                settings.laser_height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        self.x = float(self.rect.x)

        self.color = settings.laser_color
        self.speed_factor = settings.laser_speed_factor

    def update(self):
        self.x += self.speed_factor

        self.rect.x = self.x

    def draw_laser(self):
        pygame.draw.rect(self.screen, self.color, self.rect)