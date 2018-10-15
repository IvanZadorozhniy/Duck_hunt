from settings import *
images = [('images//move'+str(num)+".png" , 0.2) for num in range(1,5)]
dogAnimation = PygAnimation(images)
class Dog(pygame.sprite.Sprite):
    def __init__( self, color, x, y):
        super( Dog, self ).__init__()
        self.animation = dogAnimation
        self.animation.scale((100,100))
        self.size = self.animation.getRect()
        self.image = pygame.Surface((100, 100))
        self.image.fill((100,100,100))
        self.image.set_colorkey((100,100,100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.animation.play()
    def update(self):
        print(self.size)
        self.image.fill((100,100,100))
        self.animation.blit(self.image,(0,0))
        self.rect.x += 2