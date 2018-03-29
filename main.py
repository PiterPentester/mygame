import pygame
from settings import Settings
from ship import Ship
import game_functions as g_f
from pygame.sprite import Group
from background import Background
from alien import Alien

def init_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("My first game")
    ship = Ship(screen, game_settings)
    alien = Alien(game_settings, screen)
    background = Background(screen)
    bullets = Group()
    while True:
        g_f.check_events(game_settings, screen, ship, bullets)
        g_f.update_screen(background, ship, bullets, alien)
        ship.update()
        bullets.update()
init_game()