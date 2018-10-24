from settings import *
from math import pow
from random import randint

duckMoveHorizontal = [('images//duckBlack' + str(num) + ".png", 0.15) for num in range(1, 4)]
duckHorizontalAnimation = PygAnimation(duckMoveHorizontal)

duckFlyAngle = [('images//duckBlack' + str(num) + ".png", 0.15) for num in range(4, 7)]
duckFlyAngleAnimation = PygAnimation(duckFlyAngle)


class Duck(pygame.sprite.Sprite):
    containers = 0
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.animation = duckFlyAngleAnimation
        self.size = (width, height)
        self.animation.scale(self.size)

        self.image = pygame.Surface(self.size)
        self.image.fill(BG_COLOR_SPRITE)
        self.image.set_colorkey(BG_COLOR_SPRITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.animation.play()

        self.speed = 15
        self.speedX = randint(2, 14)
        self.speedY = self.speedXY()
        self.directionX = 1
        self.directionY = 1


    def update(self):
        self.image.fill(BG_COLOR_SPRITE)
        self.animation.blit(self.image, (0, 0))

        self.changeDirection()
        self.rect.x += self.speedX * self.directionX
        self.rect.y += self.speedY * self.directionY

    def changeDirection(self):
        if (self.rect.x <= -60 or self.rect.x > size[0] - self.size[0] + 60):
            self.directionX *= -1
            self.animation.flip(True, False)
            self.rect.x += self.speedX * self.directionX
            self.rect.y += self.speedY * self.directionY
            self.speedX = randint(2, 14)
            self.speedY = self.speedXY()

        if (self.rect.y <= -60 or self.rect.y > 450):
            self.directionY *= -1
            self.rect.x += self.speedX * self.directionX
            self.rect.y += self.speedY * self.directionY
            self.speedX = randint(2, 14)
            self.speedY = self.speedXY()

    def speedXY(self):
        #Used a formula for constant speed moving when change a direction
        return pow(self.speed * self.speed - self.speedX * self.speedX, 1 / 2)
