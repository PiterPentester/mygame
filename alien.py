import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game_settings, screen):
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load("images/bot.png")
        self.image = pygame.transform.scale(self.image, (100, 80))
        self.rect = self.image.get_rect()
    def blitme(self):
        self.screen.blit(self.image, self.rect)
