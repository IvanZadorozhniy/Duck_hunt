import pygame
from pyganim import PygAnimation
from settings import *
import random
# Load images for create animation
dogHappy_1 = [('images//dog_happy1.png', 0.3)]
dogHappy_2 = [('images//dog_happy2.png', 0.3)]
dogHappyAnimation_1 = PygAnimation(dogHappy_1)
dogHappyAnimation_2 = PygAnimation(dogHappy_2)


class HappyDog(pygame.sprite.Sprite):
    containers = pygame.sprite.RenderUpdates()

    def __init__(self, x, y, width, height):
        # Look duck class. they are similar
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.animation = dogHappyAnimation_1
        self.size = (width, height)
        self.animation.scale(self.size)

        self.image = pygame.Surface(self.size)
        self.image.fill(BG_COLOR_SPRITE)
        # using another color because image with dog found in another place
        self.image.set_colorkey(BG_COLOR_SPRITE)
        self.speed = SPEED_OF_DOG
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.directionY = 1
        self.animation.play()

        self.run = False
        self.endAnimation = False

    def update(self):
        self.image.fill(BG_COLOR_SPRITE)
        self.animation.blit(self.image, (0, 0))
        # drunk nonsense developer, but it works =)
        if self.run:
            self.animation.blit(self.image, (0, 0))
            self.rect.y -= 2 * self.directionY
            if self.rect.y < 300:
                self.directionY *= -1
            if self.rect.y >= 400:
                self.endAnimation = True
                self.run = False
                self.rect.y = 401
                self.directionY = 1
                n = random.randint(1, 3) % 3
                if n == 0:
                    self.animation.stop()
                    self.animation = dogHappyAnimation_2
                    self.animation.scale(self.size)
                    self.animation.play()
                else:
                    self.animation.stop()
                    self.animation = dogHappyAnimation_1
                    self.animation.scale(self.size)
                    self.animation.play()
        else:

            self.endAnimation = False

    def startAnimation(self):
        # using this variable for showing to main threads that it can create a new duck
        self.run = True
