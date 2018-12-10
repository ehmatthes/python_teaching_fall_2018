import pygame
from pygame.sprite import Sprite

from random import randint

class AlienShip(Sprite):
    """A class to manage the ship."""

    def __init__(self, sh_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = sh_game.screen
        self.screen_rect = sh_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at a random position on the right
        #  side of the screen
        self.rect.left = self.screen_rect.right + randint(-30, 30)
        self.rect.y = randint(0, self.screen_rect.height)

    def update(self):
        # The alien ships will always move from right to left,
        #  and randomly up and down.
        self.rect.x -= 1
        self.rect.y += randint(-5, 5)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)