from settings import *

dogMoveImg = [('images//move' + str(num) + ".png", 0.2) for num in range(1, 5)]
dogMoveAnimation = PygAnimation(dogMoveImg)
dogJumpImg = [('images//jump' + str(num) + ".png", 0.1) for num in range(1, 3)]
print(len(dogJumpImg))
dogJumpAnimation = PygAnimation([dogJumpImg[0]])
dogLandingAnimation = PygAnimation([dogJumpImg[1]])


# TODO refactoring and add speed
# TODO add a smile for Dog

class Dog(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(Dog, self).__init__()

        self.animation = dogMoveAnimation
        self.size = (width, height)
        self.animation.scale(self.size)

        self.image = pygame.Surface(self.size)
        self.image.fill((100, 100, 100))
        self.image.set_colorkey((100, 100, 100))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.stages = ["Move", "Jump", "Landing"]
        self.stage = self.stages[0]
        self.animation.play()

    def update(self):
        if self.animation == dogMoveAnimation:
            if self.rect.x < 250:
                self.move()
            else:
                self.animation.stop()
                self.animation = dogJumpAnimation
                self.animation.scale(self.size)
                self.animation.play()
                self.stage = self.stages[1]
        elif self.animation == dogJumpAnimation:
            if self.rect.y > 280:
                self.jump()
            else:
                self.animation.stop()
                self.animation = dogLandingAnimation
                self.animation.scale(self.size)
                self.animation.play()
                self.stage = self.stages[2]
        elif self.animation == dogLandingAnimation:
            if self.rect.y < 400:
                self.landing()
            else:
                self.animation.stop()

    def move(self):
        self.image.fill((100, 100, 100))
        self.animation.blit(self.image, (0, 0))
        self.rect.x += 3

    def jump(self):
        self.image.fill((100, 100, 100))
        self.animation.blit(self.image, (0, 0))
        self.rect.x += 4
        self.rect.y -= 8

    def landing(self):
        self.image.fill((100, 100, 100))
        self.animation.blit(self.image, (0, 0))
        self.rect.x += 1
        self.rect.y += 8

    def getStage(self):
        return self.stage
