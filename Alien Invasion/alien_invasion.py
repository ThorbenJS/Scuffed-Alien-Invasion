import sys
from time import sleep
from game_stats import GameStats
import pygame
from game_settings import Settings
from spaceship import Spaceship
from projectile import Projectile
from alien_projectile import AlienProjectile
from alien import Alien
from button import Button
from scoreboard import Scoreboard
import random

class AlienInvasion:
    """main class to handle the game"""

    def __init__(self):
        """initialize the game and create resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.backround_color = (0, 0, 30)
        self.x_position = 550
        self.y_position = 750
        self.moving = False
        self.shooting = False
        self.stats = GameStats(self)
        self.projectiles = pygame.sprite.Group()
        self.alien_projectiles = pygame.sprite.Group()
        self.sb = Scoreboard(self)
        self.aliens = pygame.sprite.Group()
        self.create_fleet()
        self.stars = self.generate_stars()
        self.play_button = Button(self, "Play", 0, 0)

        self.spaceship = Spaceship(self)




    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            self.spaceship.border_collision()
            if self.stats.game_active:
                self.spaceship.update_position()
                self.projectiles.update()
                self._update_aliens()
                self.alien_projectiles.update()
            self._update_screen()


    def _check_events(self):
        """respond to key presses and mouse events"""
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_play_button(mouse_position)

    def _check_play_button(self, mouse_position):
        if self.play_button.rect.collidepoint(mouse_position):
            self.stats.reset_stats()
            self.stats.game_active = True
            self.projectiles.empty()
            self.aliens.empty()
            self.alien_projectiles.empty()
            self.create_fleet()
            self.spaceship.x_position = 550
            self.spaceship.y_position = 750



    def _check_keydown_events(self, event):
        if event.key == pygame.K_SPACE:
            self.shooting = True
            self.fire_projectile()


    def _update_screen(self):
        self.screen.fill(self.backround_color)
        self.spaceship.draw_spaceship()
        for projectile in self.projectiles.sprites():
            projectile.draw_projectile()

        for alien in self.aliens.sprites():
            alien.draw_alien(0)

        for projectile in self.alien_projectiles.sprites():
            projectile.draw_projectile()

        self.alien_shoot()
        self.draw_stars(self.screen, self.stars)

        self.spaceship.init_healthbar()
        self.spaceship.draw_healthbar()

        self.move_stars(self.stars)

        collisions = pygame.sprite.groupcollide(self.projectiles, self.aliens, True, False)
        for alien in collisions.values():
            for a in alien:
                a.health -= 1  # Reduce health

        if not self.stats.game_active:
            self.play_button.draw_button()


        if not self.aliens:
            self.projectiles.empty()
            self.alien_projectiles.empty()
            self.create_fleet()
            self.settings.increase_speed()
            self.settings.level += 1
            self.sb.prep_level()

        self.sb.draw_scoreboard()
        print(self.settings.level)

        pygame.display.flip()



    def fire_projectile(self):
        """fire a projectile from the spaceship"""
        if len(self.projectiles) < self.settings.projectile_limit:

            new_projectile = Projectile(self)
            self.projectiles.add(new_projectile)


    def create_fleet(self):
        """create a fleet of aliens"""
        available_space_x = self.settings.screen_width - (self.settings.alien_width * 2)
        available_space_y = self.settings.screen_height // 2 - (self.settings.alien_height * 3) - self.settings.alien_height

        number_of_rows = available_space_y // (self.settings.alien_height * 2)
        number_of_aliens = available_space_x // (self.settings.alien_width * 2)
        for row_number in range(number_of_rows):
            for alien_number in range(number_of_aliens):
                self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        """create a single alien"""
        alien = Alien(self)
        alien.x_position = self.settings.alien_width + 2 * alien_number * self.settings.alien_width
        alien.y_position = self.settings.alien_height + 2 * row_number * self.settings.alien_height
        self.aliens.add(alien)

    def _update_aliens(self):
        self.check_alien_collisions()
        self.aliens.update()
        self.ship_hit()


    def ship_hit(self):
        if pygame.sprite.spritecollideany(self.spaceship, self.aliens):
            if self.settings.health > 0:
                self.settings.health -= 1
                self.screen.fill((50, 0, 0))
                pygame.display.flip()
                self.screen.fill(self.settings.backround_color)

        elif pygame.sprite.spritecollideany(self.spaceship, self.alien_projectiles):
            if self.settings.health > 0:
                self.settings.health -= 1
                self.screen.fill((50, 0, 0))
                pygame.display.flip()
                self.screen.fill(self.settings.backround_color)


        if self.settings.health == 0:
            self.stats.game_active = False



    def check_alien_collisions(self):
        if self.settings.collision:
            for alien in self.aliens.sprites():
                alien.y_position += self.settings.fleet_drop_speed
                alien.rect.y = alien.y_position

            self.settings.collision = False

    def alien_shoot(self):
        for b in self.aliens.sprites():
            if len(self.alien_projectiles) < self.settings.alien_projectile_limit:
                if random.randint(0, 10000) < 1:
                    projectile = AlienProjectile(self)
                    projectile.x_position = b.x_position
                    projectile.y_position = b.y_position
                    self.alien_projectiles.add(projectile)


# MISCALLENOUS FUNCTIONS ************************************************************************************************
    def generate_stars(self):
        """Generates a list of star positions for the background."""
        import random
        stars = []
        for _ in range(100):
            x = random.randint(0, self.settings.screen_width)
            y = random.randint(0, self.settings.screen_height)
            stars.append([x, y])
        return stars


    def draw_stars(self, screen, stars):
        """Draws the stars on the given screen."""
        for star in stars:
            pygame.draw.circle(screen, (255, 255, 255), star, 2)


    def move_stars(self, stars):
        """Moves the stars downwards and wraps them around the screen."""
        if self.stats.game_active:
            if pygame.key.get_pressed()[pygame.K_a]:
                for star in stars:
                    star[0] += 0.025

            elif pygame.key.get_pressed()[pygame.K_d]:
                for star in stars:
                    star[0] -= 0.025

            elif pygame.key.get_pressed()[pygame.K_w]:
                for star in stars:
                    star[1] += 0.025

            elif pygame.key.get_pressed()[pygame.K_s]:
                for star in stars:
                    star[1] -= 0.025



if __name__ == '__main__':
    AlienInvasion().run_game()

