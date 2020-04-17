"""Make a game that begins with a rocket in the center of the screen. Allow
the player to move the rocket up, down, left, or right using the four arrow
keys. Make sure the rocket never moves beyond any edge of the screen."""

import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Rocket Game")

    bg_color = (135, 206, 235)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)

        pygame.display.flip()


run_game()