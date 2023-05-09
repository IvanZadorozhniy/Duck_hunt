import pygame
from settings import *


class Bullet(pygame.sprite.Sprite):
    containers = pygame.sprite.RenderUpdates()

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.size = (65, 50)
        self.image = pygame.Surface(self.size)
        self.image.fill(BLACK)
        self.myfont = pygame.font.SysFont('Duck Hunt', 25)
        self.surface_shot = self.myfont.render("SHOT", False, WHITE, (5, 5, 5))
        self.bullet_surface = pygame.image.load('images/bullet.png')
        self.bullet_surface = pygame.transform.scale(
            self.bullet_surface, (10, 25))
        self.bullets = NUM_BULLETS
        for i in range(self.bullets):
            self.image.blit(self.bullet_surface, (5+8+15*i, 2))
        self.image.blit(self.surface_shot, (10, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 515

    def update(self):
        self.image.fill(BLACK)
        self.surfaceScore = self.myfont.render("SHOT", False, WHITE, (5, 5, 5))
        self.image.blit(self.surfaceScore, (10, 30))
        for i in range(self.bullets):
            self.image.blit(self.bullet_surface, (5+8+15*i, 2))

    def set_bullets(self, bullets):
        self.bullets = bullets
