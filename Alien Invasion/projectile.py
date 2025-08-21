import pygame
from pygame.sprite import Sprite
from game_settings import Settings


class Projectile(Sprite):

    def __init__(self, ai):
        super().__init__()
        self.x_position = ai.spaceship.x_position + 25  # Center the projectile on the spaceship
        self.y_position = ai.spaceship.y_position
        self.projectiles = ai.projectiles
        self.speed = Settings().projectile_speed
        self.width = Settings().projectile_width
        self.height = Settings().projectile_height
        self.color = Settings().projectile_color
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position
        self.rect.y = self.y_position

    def update(self):
        self.y_position -= self.speed
        self.rect.y = self.y_position
        for projectile in self.projectiles.copy():
            if projectile.y_position < 0:
                self.projectiles.remove(projectile)
                print("Projectile removed")


    def draw_projectile(self):
        pygame.draw.rect(
            pygame.display.get_surface(),
            self.color,
            (self.x_position, self.y_position, self.width, self.height)
        )