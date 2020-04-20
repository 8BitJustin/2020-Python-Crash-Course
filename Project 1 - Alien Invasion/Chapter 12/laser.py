import pygame
from pygame.sprite import Sprite


class Laser(Sprite):
    """Manage lasers fired from spaceship."""
    def __init__(self, settings, screen, ship):
        super(Laser, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.laser_width,
                                settings.laser_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = settings.laser_color
        self.speed_factor = settings.laser_speed_factor

    def update(self):
        self.x -= self.speed_factor

        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)