import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
    """A class to represent a single alien"""

    def __init__(self, ai_game):
        """Initialize alien and starting position"""
        super().__init__()
        self.screen = ai_game.screen 
        self.settings = ai_game.settings
        #Load alien image and set rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #Start each new alien near the top left
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 

        #Store exact x position
        self.x = float(self.rect.x)

    def update(self):
        """Move alien to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x 

    def check_edges(self):
        """Returns true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False