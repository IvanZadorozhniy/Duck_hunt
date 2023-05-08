import pygame
from settings import *

class Score(pygame.sprite.Sprite):
    containers = pygame.sprite.RenderUpdates()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.score = 0
        self.size = (130,50)
        self.image = pygame.Surface(self.size)
        self.image.fill(BLACK)
        self.myfont = pygame.font.SysFont('Duck Hunt', 20)
        self.surfaceScore = self.myfont.render(str(self.score), False, WHITE,(5,5,5))
        self.image.blit(self.surfaceScore ,(50,15))
        self.rect = self.image.get_rect()
        self.rect.x = 445
        self.rect.y = 515
    def update(self):
        self.surfaceScore = self.myfont.render(str(self.score), False, WHITE, (5, 5, 5))
        self.image.blit(self.surfaceScore, (50, 15))

        # self.image = self.myfont.render(str(self.score), False, WHITE,(5,5,5))
    def changeScore(self,bullets):
        if bullets == 2:
            self.score += 1500
        elif bullets == 1:
            self.score += 1000
        elif bullets == 0:
            self.score += 500
    def pickUp(self):
        self.score -= 1000
    def getScore(self):
        return self.score