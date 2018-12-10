import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, sh_game):
        """Initialize the ship and set its starting position."""
        self.screen = sh_game.screen
        self.screen_rect = sh_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Movement flags.
        self.moving_right = False        # Look at this

    def update(self):                    # And this 
        if self.moving_right:
            if self.rect.right < 400:
                self.rect.x += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)