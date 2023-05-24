import random
import threading

import pygame

from aim import Aim
from bullet_panel import BulletPanel
from dog import Dog
from duck import Duck
from happy_dog import HappyDog
from score_panel import ScorePanel
from round_panel import RoundPanel
from settings import (BLACK, COLOR_OF_SKY, DUCK_FLIGHT_TIME, FPS, NUM_BULLETS,
                      START_OF_DISPLAY)

# from pyganim import *
SCENE_START_POSITION = (0,0)
BG_IMAGE_POSITION = (0, 0)
DOG_START_POSITION = (0, 360)
DOG_SPRITE_SIZE = (100, 100)


def draw_sky(surface):
    surface.fill(COLOR_OF_SKY)


def draw_background_panels(surface):
    Score.draw_background(surface)
    RoundPanel.draw_background(surface)
    BulletPanel.draw_background(surface)


def draw_background_image_with_dog(surface, dogs, dog, bg_image):
    dogs.update()
    match dog.is_before_background:
        case True:
            dogs.draw(surface)
            draw_background_image(surface, bg_image)
        case False:
            draw_background_image(surface, bg_image)
            dogs.draw(surface)

def draw_background_image(surface, bg_image):
    surface.blit(bg_image, BG_IMAGE_POSITION)

def run_preview_of_game(screen: pygame.Surface, surface_display: pygame.Surface, background_image: pygame.Surface) -> None:
    """Run a preview of the game.

    Args:
        screen (pygame.Surface): The surface to draw the game onto.
        surface_display (pygame.Surface): The surface to draw the game elements onto.
        background_image (pygame.Surface): The background image of the game.

    Returns:
        None
    """
    
        
    # Create a group of dogs and add a dog to it
    dogs: pygame.sprite.Group[Dog] = pygame.sprite.Group()
    dog: Dog = Dog(
        DOG_START_POSITION[0],
        DOG_START_POSITION[1],
        DOG_SPRITE_SIZE[0],
        DOG_SPRITE_SIZE[1]
    )
    dogs.add(dog)


    clock: pygame.time.Clock = pygame.time.Clock()
    # Run the game until it's no longer running or there are no more dogs
    while bool(dogs):
        # Fill the surface display with the color of the sky
        # Fill the panels by Black color
        # Update the dogs and check if they are before or after the background
        draw_sky(surface_display)
        draw_background_panels(surface_display)
        draw_background_image_with_dog(surface_display, dogs, dog, background_image)

        # Draw the surface display onto the screen and update the display
        screen.blit(surface_display, SCENE_START_POSITION)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Tick the clock to maintain the FPS
        clock.tick(FPS)


def game(screen, surface_display, background_image):

    def duckFlyAway():
        if duck.life:
            nonlocal bullets
            bullets=0
            round_panel.add_attempt(False)
            score_panel.penalty()
            duck.fly_away()
    
 
    ducks = pygame.sprite.Group()
    duck = Duck(-40, -40, 55, 55)
    ducks.add(duck)
    
    hDogs = pygame.sprite.Group()
    hDog = HappyDog(270, 400, 100, 100)
    hDogs.add(hDog)
    
    aim = Aim(-40, -40)
    
    score_panel = ScorePanel()
    bullets_panel = BulletPanel()
    round_panel = RoundPanel()
    
    all_sprites = pygame.sprite.RenderUpdates()
    all_sprites.add(ducks, hDogs, aim, score_panel, bullets_panel, round_panel)
    
    
    bullets = NUM_BULLETS
        
    pygame.mouse.set_visible(False)


    clock = pygame.time.Clock()  # clock allows to do delay for repaint of screen

    draw_sky(surface_display)
    draw_background_image(surface_display, background_image)
    
    # show surfaceDisplay on the screen
    screen.blit(surface_display, START_OF_DISPLAY)

    # Designing timer for duck. When it ticks then the duck flies away
    threading.Timer(DUCK_FLIGHT_TIME, duckFlyAway).start()

    while True:

        # Checking the completion of the animation of a happy dog to create a
        # new duck or checking that the duck is alive, but she flew away
        if (hDog.endAnimation) or (duck.life and not duck.alive()):

            duck.set_place(random.randrange(0, 600),
                           random.randrange(300, 400))
            ducks.add(duck)
            all_sprites.add(ducks)

            bullets = NUM_BULLETS
            bullets_panel.set_bullets(bullets)
            try:
                timerFlyingDuck.cancel()
            except Exception:
                print(Exception)
            timerFlyingDuck = threading.Timer(DUCK_FLIGHT_TIME, duckFlyAway)
            timerFlyingDuck.start()


        if not duck.alive() and not hDog.run and not duck.life:
            round_panel.add_attempt(True)
            hDog.startAnimation()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:

                aim.update_position(event.pos)
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and bullets > 0
            ):
                bullets -= 1
                bullets_panel.set_bullets(bullets)

                aim.play_sound_shot()  # Trigger shot sound
                # Check whether the user got into the duck

                if duck.is_hit(event.pos):
                    score_panel.change_score(bullets)

        # Repainting sprites
        all_sprites.clear(screen, surface_display)
        all_sprites.update()
        dirty = all_sprites.draw(screen)

        # Updating screen for user
        screen.blit(background_image, SCENE_START_POSITION)
        pygame.display.update(dirty)

        # Delay loop
        clock.tick(FPS)

    
