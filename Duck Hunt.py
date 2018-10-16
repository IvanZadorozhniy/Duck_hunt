from utils import *

bg = pygame.image.load("images//background.png").convert()
bg = pygame.transform.scale(bg, screen.get_size())
bg.set_colorkey(bg.get_at((0,0)))


# screen.fill((61, 191, 255))

disp = pygame.Surface(screen.get_size())


dog = Dog(0, 360, 100, 100)
duck = Duck(-40, -40, 40, 40)
dogs = pygame.sprite.Group()
ducks = pygame.sprite.Group()
dogs.add(dog)
ducks.add(duck)

running = True
clock = pygame.time.Clock()

while running:
    disp.fill((61, 191, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dogs.update()
    if dog.getStage() == "Landing":

        dogs.draw(disp)
        ducks.update()
        ducks.draw(disp)
        disp.blit(bg, (0, 0))

    else:
        disp.blit(bg, (0, 0))
        dogs.draw(disp)



    screen.blit(disp, (0, 0))


    pygame.display.update()
    clock.tick(30)
pygame.quit()


