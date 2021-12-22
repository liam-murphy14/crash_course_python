"""Module for the player's ship"""

# downloaded modules
import pygame
from pygame.sprite import Sprite 

class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship with starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # start each ship at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom 

        # float value of x
        self.x = float(self.rect.x)

        # movement flags
        self.moving_left = False
        self.moving_right = False

        # settings object
        self.settings = ai_game.settings

    def update(self):
        """Update the ship's position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = int(self.x)

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship onscreen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)