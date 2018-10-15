from utils import *

bg = pygame.image.load("images//background.png")
bg = pygame.transform.scale(bg,screen.get_size())
screen.blit(bg, (0, 0))
dog = Dog(BLACK, 0, 360)
dogs = pygame.sprite.Group()
dogs.add(dog)
running = True
clock = pygame.time.Clock()


while running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dogs.update()
    dogs.draw(screen)
    pygame.display.update()
    clock.tick(30)
pygame.quit()