from settings import *
from duck import *
from dog import *

all = pygame.sprite.RenderUpdates()
Duck.containers = all
Dog.containers = all
def RunStartingVideoOfGame():
    dogs = pygame.sprite.Group()
    dog = Dog(0, 360, 100, 100)
    dogs.add(dog)

    running = True
    clock = pygame.time.Clock()

    while running and bool(dogs):
        surfaceDisplay.fill((61, 191, 255))

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


def quit():
    pygame.quit()


def game():
    ducks = pygame.sprite.Group()

    duck = Duck(-40, -40, 40, 40)

    ducks.add(duck)

    all.add(ducks)

    running = True
    clock = pygame.time.Clock()
    surfaceDisplay.fill((61, 191, 255))
    surfaceDisplay.blit(bg, (0, 0))
    screen.blit(surfaceDisplay, (0, 0))
    # pygame.display.flip()
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all.clear(screen, surfaceDisplay)
        all.update()

        dirty = all.draw(screen)
        screen.blit(bg, (0, 0))
        pygame.display.update(dirty)
        clock.tick(50)
    if not running:
        quit()
