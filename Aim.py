import pygame
from pyganim import PygAnimation
from settings import *

aimImages = [("images//aim.png",0.1)]
aimAnimation = PygAnimation(aimImages)

class Aim(pygame.sprite.Sprite):
    containers = pygame.sprite.RenderUpdates()

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.animation = aimAnimation
        self.size = (AIM_SIZE, AIM_SIZE)
        self.animation.scale(self.size)
        self.image = pygame.Surface(self.size)
        self.image.fill(BG_COLOR_SPRITE)
        self.image.set_colorkey(BG_COLOR_SPRITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animation.play()
        self.sound_shoot = pygame.mixer.Sound("music//shoot.ogg")
        self.sound_shoot.set_volume(1)
    
    def update(self):
        self.image.fill(BG_COLOR_SPRITE)
        self.animation.blit(self.image, (0, 0))

    def updatePosition(self,pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    
    def play_sound_shot(self):
        pygame.mixer.Sound.play(self.sound_shoot)