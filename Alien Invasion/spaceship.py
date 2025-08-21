import pygame
from game_settings import Settings

class Spaceship:

    def __init__(self, ai):
        self.x_position = ai.x_position
        self.y_position = ai.y_position
        self.rect = pygame.Rect(self.x_position, self.y_position, 50, 50)
        self.rect.x = self.x_position
        self.rect.y = self.y_position
        self.settings = ai.settings
        self.spaceship_pixel_matrix = [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1]
        ]
        self.moving = False
        self.helttijuuh = Settings().health


    def update_position(self):

        if pygame.key.get_pressed()[pygame.K_a]:
            self.x_position -= self.settings.movement_speed
            self.rect.x = self.x_position
            self.moving = True
        if pygame.key.get_pressed()[pygame.K_d]:
            self.x_position += Settings().movement_speed
            self.rect.x = self.x_position
            self.moving = True
        if pygame.key.get_pressed()[pygame.K_w]:
            self.y_position -= Settings().movement_speed
            self.rect.y = self.y_position
            self.moving = True
        if pygame.key.get_pressed()[pygame.K_s]:
            self.y_position += Settings().movement_speed
            self.rect.y = self.y_position
            self.moving = True


    def draw_spaceship(self):
        for row_index, row in enumerate(self.spaceship_pixel_matrix):
            for col_index, pixel in enumerate(row):
                if pixel == 1:
                    pygame.draw.rect(
                        pygame.display.get_surface(),
                        (self.settings.ship_color),  # White color for the spaceship
                        (col_index * 10 + self.x_position, row_index * 10 + self.y_position, 10, 10)


                    )

    def draw_healthbar(self):
        for i in range(self.settings.health):
            pygame.draw.rect(pygame.display.get_surface(), (self.settings.alien_color), (30 + i, 740, 5, 10))

    def init_healthbar(self):
        for i in range(self.helttijuuh):
            pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), (30 + i, 740, 5, 10))

    def border_collision(self):

        """check for border collisions and adjust position"""
        if self.x_position < 0:
            self.x_position = 0
        elif self.x_position > Settings().screen_width - 50:
            self.x_position = Settings().screen_width - 50

        if self.y_position > 750:
            self.y_position = 750
        elif self.y_position < Settings().screen_height / 2:
            self.y_position = Settings().screen_height / 2