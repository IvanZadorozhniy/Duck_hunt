from utils import *
all = pygame.sprite.RenderUpdates()
Duck.containers = all
Dog.containers = all
#TODO: Refactoring code. Change function and reduce the quantity of code


def run():
    bg = pygame.image.load("images//background.png").convert()
    bg = pygame.transform.scale(bg, screen.get_size())
    bg.set_colorkey(bg.get_at((0, 0)))

    # screen.fill((61, 191, 255))

    disp = pygame.Surface(screen.get_size())
    dog = Dog(0, 360, 100, 100)

    dogs = pygame.sprite.Group()

    dogs.add(dog)


    running = True
    clock = pygame.time.Clock()

    while running and bool(dogs):
        disp.fill((61, 191, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        dogs.update()
        if dog.getStage() == "Landing":

            dogs.draw(disp)

            disp.blit(bg, (0, 0))

        else:
            disp.blit(bg, (0, 0))
            dogs.draw(disp)



        screen.blit(disp, (0, 0))


        pygame.display.update()
        clock.tick(30)
    if not running:
        quit()
def quit():
    pygame.quit()


def game():
    bg = pygame.image.load("images//background.png").convert()
    bg = pygame.transform.scale(bg, screen.get_size())
    bg.set_colorkey(bg.get_at((0, 0)))

    # screen.fill((61, 191, 255))
    ducks = pygame.sprite.Group()


    disp = pygame.Surface(screen.get_size())


    Duck.containers = all
    duck = Duck(-40, -40, 40, 40)

    ducks.add(duck)

    all.add(ducks)

    running = True
    clock = pygame.time.Clock()
    disp.fill((61, 191, 255))
    disp.blit(bg, (0, 0))
    screen.blit(disp, (0, 0))
    pygame.display.flip()
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all.clear(screen, disp)
        all.update()

        dirty = all.draw(screen)
        screen.blit(bg, (0, 0))
        pygame.display.update(dirty)
        clock.tick(30)
    pygame.quit()

if pygame.display.get_init():
    run()

if pygame.display.get_init():
    game()

