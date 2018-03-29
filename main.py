import pygame
from settings import Settings
from ship import Ship
import game_functions as g_f
from pygame.sprite import Group
from background import Background

def init_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("My first game")
    ship = Ship(screen, game_settings)
    aliens = Group()
    background = Background(screen)
    bullets = Group()
    g_f.create_fleet(game_settings, screen, aliens)
    while True:
        g_f.check_events(game_settings, screen, ship, bullets)
        g_f.update_screen(background, ship, bullets, aliens, screen)
        ship.update()
        bullets.update()
init_game()