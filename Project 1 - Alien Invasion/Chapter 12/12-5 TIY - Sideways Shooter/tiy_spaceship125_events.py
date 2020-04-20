import sys
import pygame
from laser import Laser


def check_keydown_events(event, settings, screen, ship, lasers):
    """Responds to key presses."""
    if event.key == pygame.K_RIGHT:
        # Move ship to right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move ship to left.
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # Move ship up.
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Move ship down.
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        fire_laser(settings, screen, ship, lasers)


def fire_laser(settings, screen, ship, lasers):
    """Fire new bullet if limit not yet reached."""
    if len(lasers) < settings.lasers_allowed:
        new_laser = Laser(settings, screen, ship)
        lasers.add(new_laser)


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        # Stop moving ship to right.
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # Stop moving ship to left.
        ship.moving_left = False
    if event.key == pygame.K_UP:
        # Stop moving ship up.
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        # Stop moving ship down.
        ship.moving_down = False


def check_events(settings, screen, ship, lasers):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, lasers)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_lasers(lasers):
    """Updates position of bullets and get rid of old bullets."""
    # Get rid of bullets that have disappeared.
    for laser in lasers.copy():
        if laser.rect.bottom <= 0:
            lasers.remove(laser)


def update_screen(settings, screen, ship, lasers):
    # Update images on the screen and flip to the new screen.
    screen.fill(settings.bg_color)

    # Redraw all bullets behind ship and aliens.
    for laser in lasers.sprites():
        laser.draw_laser()

    # Draws ship.
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
