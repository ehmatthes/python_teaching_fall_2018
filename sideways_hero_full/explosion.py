import pygame

class Explosion:
    """A class to manage the explosion."""

    def __init__(self, sh_game, ship):
        """Initialize the explosion and set its starting position."""
        self.screen = sh_game.screen
        self.screen_rect = sh_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/explosion.bmp')
        self.rect = self.image.get_rect()

        # Start each explosion at the ship's nose.
        self.rect.center = ship.rect.midright

    def blitme(self):
        """Draw the explosion at its current location."""
        self.screen.blit(self.image, self.rect)