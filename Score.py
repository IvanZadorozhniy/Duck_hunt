from settings import *

class Score(pygame.sprite.Sprite):
    containers = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.score = 0
        self.size = (100,50)
        self.image = pygame.Surface(self.size)
        self.image.fill(BG_COLOR_SPRITE)
        self.image.set_colorkey(BG_COLOR_SPRITE)
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.image = myfont.render(str(self.score), False, BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    def update(self, *args):
        self.image.fill(BG_COLOR_SPRITE)
        self.image.set_colorkey(BG_COLOR_SPRITE)
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.image = myfont.render(str(self.score), False, BLACK)
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