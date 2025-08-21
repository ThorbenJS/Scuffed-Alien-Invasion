import pygame.font

class Scoreboard:
    def __init__(self, ai):
        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai.settings
        self.stats = ai.stats

        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont("Game Score", 48)
        self.prep_score()
        self.prep_level()


    def prep_score(self):
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def draw_scoreboard(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.level_text, self.level_text_rect)

    def prep_level(self):
        self.level_image = self.font.render(str(self.settings.level), True, (50, 200, 200), None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 60

        self.level_text = self.font.render("Level:", True, (50, 200, 200), None)
        self.level_text_rect = self.level_text.get_rect()
        self.level_text_rect.right = self.screen_rect.right - 50
        self.level_text_rect.top = 60
