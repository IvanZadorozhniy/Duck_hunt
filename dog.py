import pygame
from pyganim import PygAnimation
from settings import *

#load images for create of animation
dogMoveImg = [('images//move' + str(num) + ".png", 0.2) for num in range(1, 5)]
dogMoveAnimation = PygAnimation(dogMoveImg)

dogJumpImg = [('images//jump' + str(num) + ".png", 0.1) for num in range(1, 3)]
dogJumpAnimation = PygAnimation([dogJumpImg[0]])

dogLandingAnimation = PygAnimation([dogJumpImg[1]])


# TODO refactoring and add speed
# TODO add a smile for Dog

class Dog(pygame.sprite.Sprite):
    containers = pygame.sprite.RenderUpdates()

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.animation = dogMoveAnimation
        self.size = (width, height)
        self.animation.scale(self.size)

        self.image = pygame.Surface(self.size)
        self.image.fill(BG_COLOR_SPRITE)
        self.image.set_colorkey(BG_COLOR_SPRITE)
        self.speed = SPEED_OF_DOG
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.stages = ["Move", "Jump", "Landing"]
        
        self.stage = self.stages[0]
        self.animation.play()

    def update(self):
        # update this sprite
        self.image.fill(BG_COLOR_SPRITE)
        self.animation.blit(self.image, (0, 0))
        self.checkAnimation()

    def checkAnimation(self):
        # check the animation and change them according to the conditions
        if self.animation == dogMoveAnimation:
            if self.rect.x < END_OF_DOG_WAY:
                self.move()
            else:
                self.animation.stop()
                self.animation = dogJumpAnimation
                self.animation.scale(self.size)
                self.animation.play()
                self.stage = self.stages[1]
        elif self.animation == dogJumpAnimation:
            if self.rect.y > END_OF_DOG_JUMP:
                self.jump()
            else:
                self.animation.stop()
                self.animation = dogLandingAnimation
                self.animation.scale(self.size)
                self.animation.play()
                self.stage = self.stages[2]
        elif self.animation == dogLandingAnimation:
            if self.rect.y < END_OF_DOG_LANDING:
                self.landing()
            else:
                self.animation.stop()
                self.kill()

    def move(self):
        # change position when dog moves
        self.rect.x += self.speed

    def jump(self):
        # change position when dog Jump
        self.rect.x += self.speed * 2
        self.rect.y -= self.speed * 3

    def landing(self):
        # change position when dog landing
        self.rect.x += self.speed
        self.rect.y += self.speed * 3

    def getStage(self):
        return self.stage
