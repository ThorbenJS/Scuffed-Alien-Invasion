import pygame
import random
from pygame.sprite import Sprite
from game_settings import Settings
from scoreboard import Scoreboard

class Alien(Sprite):

    def __init__(self, ai):
        super().__init__()
        self.settings = ai.settings
        self.aliens = ai.aliens
        self.alien_pixel_matrix = [
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]

        self.damaged_alien_pixel_matrix_1 = [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0]
        ]

        self.damaged_alien_pixel_matrix_2 = [
            [0, 0, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0]
        ]

        self.x_position = 10
        self.y_position = 10
        self.screen = ai.screen
        self.health = 2
        self.image = pygame.Surface((self.settings.alien_width, self.settings.alien_height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position
        self.rect.y = self.y_position
        self.stats = ai.stats
        self.scoreboard = ai.sb



    def draw_alien(self, x):
        for row_index, row in enumerate(self.alien_pixel_matrix):
            for col_index, pixel in enumerate(row):
                if pixel == 1:
                    pygame.draw.rect(
                        self.screen,
                        (self.settings.alien_color),  # White color for the spaceship
                        (col_index * 10 + self.x_position + x, row_index * 10 + self.y_position, 10, 10)
                    )
    def update(self):
        """update the position of the alien"""
        self.x_position += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x_position
        self.check_border_collision()
        if self.health == 1:
            self.alien_pixel_matrix = random.choice([self.damaged_alien_pixel_matrix_1, self.damaged_alien_pixel_matrix_2])
        elif self.health <= 0:
            self.stats.score += self.settings.alien_kill_score
            self.scoreboard.prep_score()
            self.aliens.remove(self)

    def check_border_collision(self):
        if self.x_position < 0 or self.x_position > self.settings.screen_width - self.settings.alien_width:
            self.settings.fleet_direction *= -1
            self.settings.collision = True
        if self.y_position > self.settings.screen_height - self.settings.alien_height:
            self.stats.game_active = False




            


