import pygame


class Megaman:

    def __init__(self, screen):
        """Initialize megaman and set it's starting position."""
        self.screen = screen

        # Load the megaman image and get it's rect.
        self.image = pygame.image.load('images/megaman.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draw the character at it's current location."""
        self.screen.blit(self.image, self.rect)
