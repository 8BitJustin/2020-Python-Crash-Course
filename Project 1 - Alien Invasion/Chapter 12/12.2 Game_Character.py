import sys
import pygame
from megaman import Megaman


def blue_sky():
    # Initializes game, and creates screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")

    # Make character.
    mega = Megaman(screen)

    # Sets screen color.
    bg_color = (135, 206, 235)

    # Starts main loop of game.
    while True:

        # Watch for keyboard/mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through loop.
        screen.fill(bg_color)

        mega.blitme()

        # Makes most recently drawn screen visible.
        pygame.display.flip()


blue_sky()