"""Make a Pygame file that creates an empty screen. In the event loop,
print the event.key attribute whenever a pygame.KEYDOWN event is detected.
Run program, press various keys to see how Pygame responds."""

import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Keypress")

    bg_color = (135, 206, 235)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                print(event.key)
                print(event.scancode)
                print()

        screen.fill(bg_color)

        pygame.display.flip()


run_game()