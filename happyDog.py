from settings import *

# Load images for create animation
dogHappy = [('images//happyDog.png', 0.2)]
dogHappyAnimation = PygAnimation(dogHappy)


class HappyDog(pygame.sprite.Sprite):
    containers = 0

    def __init__(self, x, y, width, height):
        # Look duck class. they are similar
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.animation = dogHappyAnimation
        self.size = (width, height)
        self.animation.scale(self.size)

        self.image = pygame.Surface(self.size)
        self.image.set_colorkey((163, 239, 165)) # using another color because image with dog found in another place
        self.speed = SPEED_OF_DOG
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.directionY = 1
        self.animation.play()

        self.run = False
        self.endAnimation = False

    def update(self):
        # drunk nonsense developer, but it works =)
        if self.run:
            self.animation.blit(self.image, (0, 0))
            self.rect.y -= 2 * self.directionY
            if self.rect.y < 300:
                self.directionY *= -1
            if self.rect.y >= 400:
                self.endAnimation = True
                self.run = False
                self.rect.y = 401
                self.directionY = 1
        else:
            self.endAnimation = False

    def startAnimation(self):
        self.run = True # using this variable for showing to main threads that it can create a new duck
