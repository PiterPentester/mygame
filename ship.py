import pygame

class Ship():
    def __init__(self, screen, game_settings):
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load("images/ship.png")
        self.image = pygame.transform.scale(self.image, (240, 140))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.game_settings.ship_speed_factor
