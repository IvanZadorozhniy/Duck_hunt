import random
import threading

import pygame
from Aim import Aim
from Score import Score
from dog import Dog

from duck import Duck
from happyDog import HappyDog
from settings import *


import pygame
# from pyganim import *



def RunStartingVideoOfGame(screen, surface_display, background_image):
    dogs = pygame.sprite.Group()
    dog = Dog(0, 360, 100, 100)
    dogs.add(dog)

    running = True
    clock = pygame.time.Clock()

    while running and bool(dogs):
        surface_display.fill(COLOR_OF_SKY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        dogs.update()
        if dog.is_before_background:
            dogs.draw(surface_display)
            surface_display.blit(background_image, (0, 0))
        else:
            surface_display.blit(background_image, (0, 0))
            dogs.draw(surface_display)


        screen.blit(surface_display, (0, 0))
        pygame.display.update()
        clock.tick(FPS)
    if not running:
        quit()


def game(screen, surface_display, background_image):
    def runHappyDog():
        hDog.startAnimation()

    def duckFlyAway():
        if duck.life:
            score.pickUp()
            duck.flyAway()
    pygame.mouse.set_visible(False)
    bullets = NUM_BULLETS
    score = 0
    ducks = pygame.sprite.Group()
    duck = Duck(-40, -40, 55, 55)
    aim = Aim(-40, -40)
    score = Score()
    hDogs = pygame.sprite.Group()
    hDog = HappyDog(270, 400, 100, 100)

    hDogs.add(hDog)
    ducks.add(duck)
    all = pygame.sprite.RenderUpdates()
    all.add(ducks)
    all.add(hDogs)
    all.add(aim)
    all.add(score)
    running = True

    clock = pygame.time.Clock()  # clock allows to do delay for repaint of screen

    surface_display.fill(COLOR_OF_SKY)  # this surface is main field for paint
    surface_display.blit(background_image, START_OF_DISPLAY)
    screen.blit(surface_display, START_OF_DISPLAY)  # show surfaceDisplay on the screen

    timerFlyingDuck = threading.Timer(DUCK_FLIGHT_TIME,
                                      duckFlyAway).start()  # Designing timer for duck. When it ticks then the duck flies away

    while running:

        # Checking the completion of the animation of a happy dog to create a
        # new duck or checking that the duck is alive, but she flew away
        if (hDog.endAnimation) or (duck.life and not duck.alive()):
            # DELAY
            # Set new random place for duck
            # Adding duck to groups sprite ducks
            # adding this group to all group
            # restart timer
            # time.sleep(DELAY_DUCK_APPEARANCE)

            duck.setPlace(random.randrange(0, 600), random.randrange(0, 200))

            ducks.add(duck)
            all.add(ducks)

            bullets = NUM_BULLETS
            try:
                timerFlyingDuck.cancel()
            except Exception:
                print(Exception)
            timerFlyingDuck = threading.Timer(DUCK_FLIGHT_TIME, duckFlyAway)
            timerFlyingDuck.start()

        # Checking life of duck and checking launch of happy dog
        # if there is no duck in any group and
        # the duck is dead
        # and the happy dog is not running
        # then run the happy dog
        if not duck.alive() and not hDog.run and not duck.life:
            runHappyDog()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                
                aim.updatePosition(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left button of mouse
                    if bullets > 0:
                        bullets -= 1
                        aim.play_sound_shot()  # Trigger shot sound
                        gotin = duck.checkClick(event.pos)  # Check whether the user got into the duck
                        if gotin:
                            score.changeScore(bullets)


        # Repainting sprites
        all.clear(screen, surface_display)
        all.update()
        dirty = all.draw(screen)

        # Updating screen for user
        screen.blit(background_image, START_OF_DISPLAY)
        pygame.display.update(dirty)

        # Delay loop
        clock.tick(FPS)

    if not running:
        quit()


def quit():
    pygame.quit()
