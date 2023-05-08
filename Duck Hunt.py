import pygame
from settings import *


def set_up_pygame():
    pygame.init()
    pygame.font.init()
    size = [WINDOW_HEIGHT, WINDOW_WIDHT]
    screen = pygame.display.set_mode(size)

    bg = pygame.image.load("images//background.png").convert()
    bg = pygame.transform.scale(bg, screen.get_size())
    bg.set_colorkey(bg.get_at((0, 0)))

    surface_display = pygame.Surface(screen.get_size())


    pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**6)
    background_music = pygame.mixer.Sound("music//8-bit.ogg")
    background_music.set_volume(0.3)
    
    background_music.play(-1)
    return screen, surface_display, bg, background_music

screen, surface_display, bg, background_music = set_up_pygame()

from utils import RunStartingVideoOfGame, game

# if pygame.display.get_init():
#     RunStartingVideoOfGame(screen, surface_display, bg)

if pygame.display.get_init():
    game(screen, surface_display, bg)
