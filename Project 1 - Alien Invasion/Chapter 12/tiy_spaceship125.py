import pygame


class Spaceship:

    def __init__(self, screen):
        self.screen = screen

        # Loads ship image and gets it's rect.
        self.image = pygame.image.load('images/spaceship125-reduced.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Starts ship at middle of screen.
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # Movement flag.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right/3:
            self.rect.centerx += 1
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        elif self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def blitme(self):
        """Draws ship at current location."""
        self.screen.blit(self.image, self.rect)

