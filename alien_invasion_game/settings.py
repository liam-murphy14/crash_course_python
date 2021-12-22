"""Module to control settings for Alien Invasion game"""

class Settings:
    """A class to store Alien Invasion settings"""

    def __init__(self):
        """initialize the game's static settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.number_bullets_allowed = 5

        #alien settings
        self.fleet_drop_speed = 10

        self.scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize dynamic settings"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.scale 
        self.bullet_speed *= self.scale 
        self.alien_speed *= self.scale
        self.alien_points = int(self.alien_points * self.score_scale)