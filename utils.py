import threading

from settings import *
from duck import *
from dog import *
from happyDog import *
from Aim import *
all = pygame.sprite.RenderUpdates()
Duck.containers = all
Dog.containers = all
Aim.containers = all
HappyDog.containers = all


def RunStartingVideoOfGame():
    dogs = pygame.sprite.Group()
    dog = Dog(0, 360, 100, 100)
    dogs.add(dog)

    running = True
    clock = pygame.time.Clock()

    while running and bool(dogs):
        surfaceDisplay.fill(COLOR_OF_SKY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        dogs.update()
        if dog.getStage() == "Landing":

            dogs.draw(surfaceDisplay)

            surfaceDisplay.blit(bg, (0, 0))

        else:
            surfaceDisplay.blit(bg, (0, 0))
            dogs.draw(surfaceDisplay)

        screen.blit(surfaceDisplay, (0, 0))

        pygame.display.update()
        clock.tick(45)
    if not running:
        quit()


def game():
    def runHappyDog():
        hDog.startAnimation()

    def duckFlyAway():
        if duck.life:
            duck.flyAway()

    pygame.mouse.set_visible(False)
    bullets = NUM_BULLETS

    ducks = pygame.sprite.Group()
    duck = Duck(-40, -40, 40, 40)
    aim = Aim(-40,-40)
    hDogs = pygame.sprite.Group()
    hDog = HappyDog(270, 400, 100, 100)


    hDogs.add(hDog)
    ducks.add(duck)


    all.add(ducks)
    all.add(hDogs)
    all.add(aim)
    running = True

    clock = pygame.time.Clock() # clock allows to do delay for repaint of screen

    surfaceDisplay.fill(COLOR_OF_SKY) # this surface is main field for paint
    surfaceDisplay.blit(bg, START_OF_DISPLAY)
    screen.blit(surfaceDisplay, START_OF_DISPLAY) # show surfaceDisplay on the screen

    timerFlyingDuck = threading.Timer(duckFlightTime, duckFlyAway).start() # Designing timer for duck. When it ticks then the duck flies away

    while running:

        # Checking the completion of the animation of a happy dog to create a
        # new duck or checking that the duck is alive, but she flew away
        if (hDog.endAnimation) or (duck.life and not duck.alive()):
            # DELAY
            # Set new random place for duck
            # Adding duck to groups sprite ducks
            # adding this group to all group
            # restart timer
            time.sleep(DELAY_DUCK_APPEARANCE)

            duck.setPlace(random.randrange(-100,500), random.randrange(-40,200))

            ducks.add(duck)
            all.add(ducks)

            bullets = NUM_BULLETS

            timerFlyingDuck = threading.Timer(duckFlightTime, duckFlyAway)
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
                        shoot.play() # Trigger shot sound
                        duck.checkClick(event.pos) # Check whether the user got into the duck
        # if numbers of bullets equals null and duck is alive
        # then duck flies away and timer will be killed
        if (bullets == 0 and duck.life):
            duckFlyAway()
            timerFlyingDuck.cancel()

        # Repainting sprites
        all.clear(screen, surfaceDisplay)
        all.update()
        dirty = all.draw(screen)

        #Updating screen for user
        screen.blit(bg, START_OF_DISPLAY)
        pygame.display.update(dirty)

        #Delay loop
        clock.tick(35)

    if not running:
        quit()

def quit():
    pygame.quit()
