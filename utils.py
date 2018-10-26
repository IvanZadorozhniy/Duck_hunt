from settings import *
from duck import *
from dog import *
from happyDog import *

all = pygame.sprite.RenderUpdates()
Duck.containers = all
Dog.containers = all
HappyDog.containers = all


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


def game():
    def runHappyDog():
        hDog.startAnimation()

    bullets = 3
    ducks = pygame.sprite.Group()
    duck = Duck(-40, -40, 40, 40)
    hDog = HappyDog(270, 400, 100, 100)
    hDogs = pygame.sprite.Group()
    hDogs.add(hDog)
    ducks.add(duck)

    all.add(ducks)
    all.add(hDogs)
    running = True
    clock = pygame.time.Clock()
    surfaceDisplay.fill((61, 191, 255))
    surfaceDisplay.blit(bg, (0, 0))
    screen.blit(surfaceDisplay, (0, 0))
    createDuck = False
    while running:
        if hDog.endAnimation:
            duck.setPlace(random.randrange(-100,500), random.randrange(-40,200))
            ducks.add(duck)
            all.add(ducks)
            bullets = 3
        if duck.life and not duck.alive():
            time.sleep(1.0)
            duck.setPlace(random.randrange(-100, 500), random.randrange(-40, 200))
            ducks.add(duck)
            all.add(ducks)
            bullets = 3
        if not duck.alive() and not hDog.run and not duck.life:
            runHappyDog()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # левая кнопка мыши
                    if bullets > 0:
                        bullets -= 1
                        shoot.play()
                        duck.checkClick(event.pos)
        if bullets == 0:
            duck.flyAway()
        all.clear(screen, surfaceDisplay)
        all.update()

        dirty = all.draw(screen)
        screen.blit(bg, (0, 0))
        pygame.display.update(dirty)
        clock.tick(35)
    if not running:
        quit()


def quit():
    pygame.quit()
