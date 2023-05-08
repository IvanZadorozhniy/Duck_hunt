import pygame
from pyganim import *
from duck import *

running = True
clock = pygame.time.Clock()
duck = Duck(50, 400, 40, 40)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(duck)

while running:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.update()
    clock.tick(30)
pygame.quit()
