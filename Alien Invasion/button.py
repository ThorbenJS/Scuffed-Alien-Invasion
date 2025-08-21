import pygame.font


class Button:

    def __init__(self, ai, text, x, y):
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.width, self.height = 200, 50
        self.text_color = (255, 255, 255)
        self.button_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prepare_text(text)


    def prepare_text(self, text):
        self.text_image = self.font.render(text, True, self.text_color, self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)


