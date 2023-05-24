import threading

import pygame

from pyganim import PygAnimation
from settings import (BG_COLOR_SPRITE, END_OF_DOG_JUMP, END_OF_DOG_LANDING,
                      END_OF_DOG_WAY, SPEED_OF_DOG)

# load images for create of animation
dog_walk_images = [(f'images//dog_walk{num}.png', 0.2) for num in range(1, 6)]
dog_walk_animation = PygAnimation(dog_walk_images)

dog_smell_images = [("images//dog_smell.png", 0.2)]
dog_smell_animation = PygAnimation(dog_smell_images)

dog_jump_images = [(f'images//dog_jump{num}.png', 0.1) for num in range(1, 3)]
dog_jump_animation = PygAnimation([dog_jump_images[0]])
dog_landing_animation = PygAnimation([dog_jump_images[1]])


class Dog(pygame.sprite.Sprite):
    containers = pygame.sprite.RenderUpdates()

    def __init__(self, start_position_x, start_position_y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.animation = dog_walk_animation
        self.size = (width, height)
        self.animation.scale(self.size)

        self.image = pygame.Surface(self.size)
        self.image.fill(BG_COLOR_SPRITE)
        self.image.set_colorkey(BG_COLOR_SPRITE)
        self.speed = SPEED_OF_DOG
        self.rect = self.image.get_rect()
        self.rect.x = start_position_x
        self.rect.y = start_position_y
        self.animation.play()
        self.is_before_background = False

    def update(self):
        """Update this sprite for every frame"""
        self.image.fill(BG_COLOR_SPRITE)
        self.animation.blit(self.image, (0, 0))
        self.__check_animation()
        

    def __check_animation(self):
        # check the animation and change them according to the conditions
        if self.animation == dog_walk_animation:
            if self.rect.x < END_OF_DOG_WAY:
                self.move()
            else:
                self.__change_animation(dog_smell_animation)
                timer = threading.Timer(
                    0.9, self.__change_animation, (dog_jump_animation,))
                timer.start()
        elif self.animation == dog_smell_animation:
            pass
        elif self.animation == dog_jump_animation:
            if self.rect.y > END_OF_DOG_JUMP:
                self.jump()
            else:
                self.__change_animation(dog_landing_animation)
                self.is_before_background = True
        elif self.animation == dog_landing_animation:
            if self.rect.y < END_OF_DOG_LANDING:
                self.landing()
            else:
                self.animation.stop()
                self.kill()

    def move(self):
        """Changes the position of the dog when it moves."""
        self.rect.x += self.speed

    def jump(self):
        """Changes the position of the dog when it jumps."""
        # change position when dog Jump
        self.rect.x += self.speed * 2
        self.rect.y -= self.speed * 3

    def landing(self):
        """Update the position of the dog sprite when it lands.

        This function moves the dog sprite to a new position when it lands.
        The amount of horizontal and vertical movement is determined by the 
        speed attribute of the sprite."""
        self.rect.x += self.speed
        self.rect.y += self.speed * 3

    def __change_animation(self, animation):
        self.animation.stop()
        self.animation = animation
        self.animation.scale(self.size)
        self.animation.play()
