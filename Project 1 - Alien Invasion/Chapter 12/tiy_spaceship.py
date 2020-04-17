import pygame

class Spaceship:

    def __init__(self, screen):
        self.screen = screen

        # Loads ship image and gets it's rect.
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Starts ship at middle of screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draws ship at current location."""
        self.screen.blit(self.image, self.rect)