import pygame
import random
from pygame.sprite import Sprite

class AlienProjectile(Sprite):

    def __init__(self, ai):
        super().__init__()
        self.projectiles = ai.alien_projectiles
        self.x_position = 0
        self.y_position = 0
        self.speed = ai.settings.alien_projectile_speed
        self.width = ai.settings.alien_projectile_width
        self.height = ai.settings.alien_projectile_height
        self.color = ai.settings.alien_projectile_color
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position
        self.rect.y = self.y_position

    def update(self):
        self.y_position += self.speed
        self.rect.y = self.y_position
        self.rect.x = self.x_position
        for projectile in self.projectiles.copy():
            if projectile.y_position > 750:
                self.projectiles.remove(projectile)
                print("Projectile removed")
                print(self.rect.x)



    def draw_projectile(self):
        pygame.draw.rect(
            pygame.display.get_surface(),
            self.color,
            (self.x_position + 25, self.y_position + 25, self.width, self.height)
        )