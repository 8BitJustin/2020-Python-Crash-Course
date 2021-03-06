import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class that represents a single alien."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set it's starting position."""

        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set it's rect attribute.
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at it's current location."""

        self.screen.blit(self.image, self.rect)
