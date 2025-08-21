import pygame

class Settings:
    """manages the settings for Alien Invasion"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.backround_color = (0, 0, 30)


        self.ship_color = (255, 255, 50)


        self.projectile_speed = 1
        self.projectile_width = 50
        self.projectile_height = 15
        self.projectile_color = (255, 255, 255)
        self.projectile_limit = 3

        self.alien_projectile_speed = 0.7
        self.alien_projectile_width = 4
        self.alien_projectile_height = 15
        self.alien_projectile_color = (150, 200, 15)
        self.alien_projectile_limit = 6


        self.alien_color = (0, 255, 0)
        self.alien_width = 50
        self.alien_height = 30

        self.level = 1

        self.speedup_scale = 1.2

        self.movement_speed = 0.5
        self.alien_speed = 0.08
        self.health = 500
        self.fleet_drop_speed = 18
        self.fleet_direction = 1
        self.collision = False

        self.alien_kill_score = 50

    def increase_speed(self):
        self.movement_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        self.alien_kill_score *= 1.5
        self.projectile_limit += 1
        self.alien_projectile_limit += 0.4
        if self.level > 5:
            self.health = 800
        else:
            self.health = 500
