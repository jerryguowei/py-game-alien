import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """Response to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Response to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)


def fire_bullets(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit no reached yet."""
    # Create a new bullet and add it to the bullet group
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Response to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """Update image on the screen and flip to the new screen."""
    screen.fill(ai_settings.big_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    # Make the most recently draw screen visible
    pygame.display.flip()


def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets"""
    # Update bullet positions.
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
