from threading import Timer

from settings import *
from math import pow
from random import randint
from time import sleep

duckMoveHorizontal = [('images//duckBlack' + str(num) + ".png", 0.15) for num in range(1, 4)]
duckHorizontalAnimation = PygAnimation(duckMoveHorizontal)

duckFlyAngle = [('images//duckBlack' + str(num) + ".png", 0.15) for num in range(4, 7)]
duckFlyAngleAnimation = PygAnimation(duckFlyAngle)

duckWounded = [('images//duckBlack' + str(num) + ".png", 0.25) for num in range(7, 9)]
duckWoundedAnimation = PygAnimation(duckWounded)
duckHit = [('images//duckBlack9.png', 0.25)]
duckHitAnimation = PygAnimation(duckHit)


class Duck(pygame.sprite.Sprite):
    containers = 0
    stages = ["FlyInGame", "DuckHit", "DuckWounded"]

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
        self.stage = self.stages[0]
        self.animation.play()

        self.speed = 15
        self.speedX = randint(2, 14)
        self.speedY = self.speedXY()
        self.directionX = 1
        self.directionY = 1
        self.life = True

    def update(self):
        self.image.fill(BG_COLOR_SPRITE)
        self.animation.blit(self.image, (0, 0))

        if self.alive():
            self.changeDirection()

        self.rect.x += self.speedX * self.directionX
        self.rect.y += self.speedY * self.directionY
        if self.rect.y > 450 and not self.life:
            self.kill()

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
        # Used a formula for constant speed moving when change a direction
        return pow(self.speed * self.speed - self.speedX * self.speedX, 1 / 2)

    def checkClick(self, pos):
        # Check if a user has hit a bird
        heightForRect = 4
        #create rect for more often hit in the duck
        CheckRect = pygame.Rect(pos[0]-heightForRect,pos[1]-heightForRect,heightForRect*2,heightForRect*2)
        if self.rect.colliderect(CheckRect):
            self.life = False
            self.stage = self.stages[1]
            self.directionX = 0
            self.directionY = 0
            self.speedY = 5
            self.animation.stop()
            duckHitAnimation.scale(self.size)
            self.animation = duckHitAnimation
            self.animation.play()
            timer = Timer(1.0, self.startFalling)
            timer.start()

    def startFalling(self):
        self.stage = self.stages[2]
        self.directionX = 0
        self.directionY = 1
        self.speedY = 3
        self.animation.stop()
        duckWoundedAnimation.scale(self.size)
        self.animation = duckWoundedAnimation
        self.animation.play()

    def setPlace(self, x, y):
        self.rect.x = x
        self.rect.y = y
        duckFlyAngleAnimation.clearTransforms()
        self.animation = duckFlyAngleAnimation
        self.animation.scale(self.size)

        if x < 0:
            self.directionX = 1

        else:
            self.directionX = -1
            self.animation.flip(True, False)
        if y < 0:
            self.directionY = 1
        else:
            self.directionY = -1
        self.stage = self.stages[0]
        self.animation.play()
        self.speed = 15
        self.speedX = randint(2, 14)
        self.speedY = self.speedXY()

        self.life = True
    def flyAway(self):
        self.directionY = -1
        self.directionX = 0
        if self.rect.y < -self.size[1]:
            self.kill()