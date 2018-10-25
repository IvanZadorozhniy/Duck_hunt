# import
import pygame
from pyganim import *
import random

pygame.init()
size = [600, 600]
screen = pygame.display.set_mode(size)

bg = pygame.image.load("images//background.png").convert()
bg = pygame.transform.scale(bg, screen.get_size())
bg.set_colorkey(bg.get_at((0, 0)))

surfaceDisplay = pygame.Surface(screen.get_size())
pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
bgMusic = pygame.mixer.Sound("music//8-bit.ogg")
bgMusic.set_volume(0.3)
bgMusic.play()
shoot = pygame.mixer.Sound("music//shoot.ogg")
shoot.set_volume(1)

# global variable
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BG_COLOR_SPRITE = (100, 100, 100)
