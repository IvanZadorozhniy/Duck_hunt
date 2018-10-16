from settings import *
from math import tan, atan, pi, pow
from random import randint

duckMoveHorizontal = [('images//duckBlack' + str(num) + ".png", 0.15) for num in range(1, 4)]
duckHorizontalAnimation = PygAnimation(duckMoveHorizontal)

duckFlyAngle = [('images//duckBlack' + str(num) + ".png", 0.15) for num in range(4, 7)]
duckFlyAngleAnimation = PygAnimation(duckFlyAngle)


class Duck(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(Duck, self).__init__()
        self.animation = duckFlyAngleAnimation
        self.size = (width, height)
        self.animation.scale(self.size)

        self.image = pygame.Surface(self.size)
        self.image.fill((100, 100, 100))
        self.image.set_colorkey((100, 100, 100))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.stages = ["Horizontal", "FlyAngle"]
        self.stage = self.stages[0]
        self.animation.play()

        self.speed = 15
        self.speedX = randint(2, 14)
        self.speedY = self.speedXY()
        self.directionX = 1
        self.directionY = 1


    def update(self):
        self.image.fill((100, 100, 100))
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
        return pow(self.speed * self.speed - self.speedX * self.speedX, 1 / 2)
