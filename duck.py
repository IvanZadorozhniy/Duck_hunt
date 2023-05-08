from threading import Timer

import pygame
from pyganim import PygAnimation

from settings import *
from math import pow
from random import randint
from time import sleep

# Load images for creating of animations
duckMoveHorizontal = [('images//duckBlack' + str(num) + ".png", 0.15) for num in range(1, 4)]
duckHorizontalAnimation = PygAnimation(duckMoveHorizontal)

duckFlyAngle = [('images//duckBlack' + str(num) + ".png", 0.15) for num in range(4, 7)]
duckFlyAngleAnimation = PygAnimation(duckFlyAngle)

duckWounded = [('images//duckBlack' + str(num) + ".png", 0.25) for num in range(7, 9)]
duckWoundedAnimation = PygAnimation(duckWounded)

duckHit = [('images//duckBlack9.png', 0.25)]
duckHitAnimation = PygAnimation(duckHit)


class Duck(pygame.sprite.Sprite):
    containers = pygame.sprite.RenderUpdates()
    ''' 
    Args: 
        ( x, y ) - position of starting of life
        ( width, height ) - size of myself
    Properties:
        animation - determines which animation should play
        size - size of myself
        image - surface of sprite
        rect - determines position of sprite
        speed - speed of duck 
        speedX and speedY - duck speed on the axes
        directionX and directionY - determines direction of flight of duck
        life - (true or false) do myself have a life?
        FlyAway - (true or false) did duck fly away?
    '''
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

        self.speed = SPEED_DUCK
        self.speedX = randint(2, (SPEED_DUCK-1))
        self.speedY = self.speedXY()

        self.directionX = 1
        self.directionY = 1

        self.life = True
        self.FlyAway = False

        self.animation.play()

    def update(self):
        '''
        Updating duck's sprite;
        1. Fill and add image to surface
        2. if duck is alive then check of change direction
        3. Change position of duck
        4. Check end of life (or dye or fly away)
        '''
        self.image.fill(BG_COLOR_SPRITE)
        self.animation.blit(self.image, (0, 0))

        if self.alive():
            self.changeDirection()

        self.rect.x += self.speedX * self.directionX
        self.rect.y += self.speedY * self.directionY
        self.checkEndLife()

    def changeDirection(self):
        '''
        if the duck got to the border then change its direction
        and set new speedX and speedY for changing angle of flight

        '''
        if (self.rect.x <= -60 or self.rect.x > WINDOW_HEIGHT - self.size[0] + 60):
            self.directionX *= -1
            self.animation.flip(True, False)
            self.rect.x += self.speedX * self.directionX
            self.rect.y += self.speedY * self.directionY
            self.speedX = randint(2, (SPEED_DUCK-1))
            self.speedY = self.speedXY()

        if (self.rect.y <= -60 or self.rect.y > 450):
            self.directionY *= -1
            self.rect.x += self.speedX * self.directionX
            self.rect.y += self.speedY * self.directionY
            self.speedX = randint(2, (SPEED_DUCK-1))
            self.speedY = self.speedXY()

    def speedXY(self):
        # Used a formula for constant speed moving when change a direction
        return pow(self.speed * self.speed - self.speedX * self.speedX, 1 / 2)

    def checkClick(self, pos):
        # Check if a user has hit a bird
        heightForRect = HEIGHT_RECT_AIM
        #create rect for more often hit in the duck
        CheckRect = pygame.Rect(pos[0]-heightForRect,pos[1]-heightForRect,heightForRect*2,heightForRect*2)
        if self.rect.contains(CheckRect):
            print("Kill")
            print(CheckRect)
            print(self.rect)
            self.life = False
            self.directionX = 0
            self.directionY = 0
            self.animation.stop()
            # Change animation
            duckHitAnimation.scale(self.size)
            self.animation = duckHitAnimation
            self.animation.play()
            # Timer for launch falling of duck
            timer = Timer(1.0, self.startFalling)
            timer.start()
            return True
        else:
            return False

    def startFalling(self):
        '''
        Method launches animation of falling of duck

        '''
        self.directionX = 0
        self.directionY = 1
        self.speedY = SPEED_OF_FALLING_OF_DUCK
        self.animation.stop()
        duckWoundedAnimation.scale(self.size)
        self.animation = duckWoundedAnimation
        self.animation.play()

    def setPlace(self, x, y):
        '''
        (x,y) - new position of duck
         Function sets new position for duck.
         It uses when need create new duck without delete current duck
        '''
        self.rect.x = x
        self.rect.y = y

        duckFlyAngleAnimation.clearTransforms()

        self.animation = duckFlyAngleAnimation
        self.animation.scale(self.size)

        # Set orientation duck in space
        if x < 0:
            self.directionX = 1
        else:
            self.directionX = -1
            self.animation.flip(True, False)
        if y < 0:
            self.directionY = 1
        else:
            self.directionY = -1

        self.animation.play()
        self.speed = SPEED_DUCK
        self.speedX = randint(2, (SPEED_DUCK-1))
        self.speedY = self.speedXY()

        self.life = True
        self.FlyAway = False

    def flyAway(self):
        # Launch of flying away of duck
        self.directionY = -1
        self.directionX = 0
        self.FlyAway = True

    def checkEndLife(self):
        # Kill duck if condition will be satisfied
        if self.rect.y < -self.size[1] and self.FlyAway:
            self.kill()
        if self.rect.y > 450 and not self.life:
            self.kill()