from math import pow
from random import randint
from threading import Timer

import pygame

from pyganim import PygAnimation
from settings import (BG_COLOR_SPRITE, HEIGHT_RECT_AIM, SPEED_DUCK,
                      SPEED_OF_FALLING_OF_DUCK, WINDOW_HEIGHT)

# Load images for creating of animations
duck_move_horizontal = [('images//duckBlack' + str(num) + ".png", 0.15)
                      for num in range(1, 4)]
duck_horizontal_animation = PygAnimation(duck_move_horizontal)

duck_fly_angle = [('images//duckBlack' + str(num) + ".png", 0.15)
                for num in range(4, 7)]
duck_fly_angle_animation = PygAnimation(duck_fly_angle)

duck_wounded = [('images//duckBlack' + str(num) + ".png", 0.25)
               for num in range(7, 9)]
duck_wounded_animation = PygAnimation(duck_wounded)

duck_hit = [('images//duckBlack9.png', 0.25)]
duck_hit_animation = PygAnimation(duck_hit)


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
        speed_x and speed_y - duck speed on the axes
        direction_x and direction_y - determines direction of flight of duck
        life - (true or false) do myself have a life?
        fly_away - (true or false) did duck fly away?
    '''

    def __init__(self, start_pos_x, start_pos_y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.animation = duck_fly_angle_animation
        self.size = (width, height)

        self.animation.scale(self.size)

        self.image = pygame.Surface(self.size)
        self.image.fill(BG_COLOR_SPRITE)
        self.image.set_colorkey(BG_COLOR_SPRITE)

        self.rect = self.image.get_rect()
        self.rect.x = start_pos_x
        self.rect.y = start_pos_y

        self.speed = SPEED_DUCK
        self.speed_x = randint(2, (SPEED_DUCK-1))
        self.speed_y = self.speed_xy()

        self.direction_x = 1
        self.direction_y = 1

        self.life = True
        self.is_fly_away = False

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
            self.change_direction()

        self.rect.x += self.speed_x * self.direction_x
        self.rect.y += self.speed_y * self.direction_y
        self.check_end_life()

    def change_direction(self):
        '''
        if the duck got to the border then change its direction
        and set new speed_x and speed_y for changing angle of flight

        '''
        if (self.rect.x <= -60 or self.rect.x > WINDOW_HEIGHT - self.size[0] + 60):
            self.direction_x *= -1
            self.animation.flip(True, False)
            self.rect.x += self.speed_x * self.direction_x
            self.rect.y += self.speed_y * self.direction_y
            self.speed_x = randint(2, (SPEED_DUCK-1))
            self.speed_y = self.speed_xy()

        if (self.rect.y <= -60 or self.rect.y > 450):
            self.direction_y *= -1
            self.rect.x += self.speed_x * self.direction_x
            self.rect.y += self.speed_y * self.direction_y
            self.speed_x = randint(2, (SPEED_DUCK-1))
            self.speed_y = self.speed_xy()

    def speed_xy(self):
        # Used a formula for constant speed moving when change a direction
        return pow(self.speed * self.speed - self.speed_x * self.speed_x, 1 / 2)

    def check_click(self, pos):
        # create rect for more often hit in the duck
        aim_rect = pygame.Rect(
            pos[0]-HEIGHT_RECT_AIM, pos[1]-HEIGHT_RECT_AIM, HEIGHT_RECT_AIM*2, HEIGHT_RECT_AIM*2)
        if self.rect.contains(aim_rect):
            self.life = False
            self.direction_x = 0
            self.direction_y = 0
            self.animation.stop()
            # Change animation
            duck_hit_animation.scale(self.size)
            self.animation = duck_hit_animation
            self.animation.play()
            # Timer for launch falling of duck
            timer = Timer(1.0, self.start_falling)
            timer.start()
            return True
        else:
            return False

    def start_falling(self):
        '''
        Method launches animation of falling of duck

        '''
        self.direction_x = 0
        self.direction_y = 1
        self.speed_y = SPEED_OF_FALLING_OF_DUCK
        self.animation.stop()
        duck_wounded_animation.scale(self.size)
        self.animation = duck_wounded_animation
        self.animation.play()

    def set_place(self, pos_x, pos_y):
        '''
        (x,y) - new position of duck
         Function sets new position for duck.
         It uses when need create new duck without delete current duck
        '''
        self.rect.x = pos_x
        self.rect.y = pos_y

        duck_fly_angle_animation.clearTransforms()

        self.animation = duck_fly_angle_animation
        self.animation.scale(self.size)

        # Set orientation duck in space
        if pos_x < 0:
            self.direction_x = 1
        else:
            self.direction_x = -1
            self.animation.flip(True, False)
        if pos_y < 0:
            self.direction_y = 1
        else:
            self.direction_y = -1

        self.animation.play()
        self.speed = SPEED_DUCK
        self.speed_x = randint(2, (SPEED_DUCK-1))
        self.speed_y = self.speed_xy()

        self.life = True
        self.is_fly_away = False

    def fly_away(self):
        # Launch of flying away of duck
        self.direction_y = -1
        self.direction_x = 0
        self.is_fly_away = True

    def check_end_life(self):
        # Kill duck if condition will be satisfied
        if self.rect.y < -self.size[1] and self.fly_away:
            self.kill()
        if self.rect.y > 450 and not self.life:
            self.kill()
