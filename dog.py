from settings import *

dogMoveImg = [('images//move' + str(num) + ".png", 0.2) for num in range(1, 5)]
dogMoveAnimation = PygAnimation(dogMoveImg)
dogJumpImg = [('images//jump' + str(num) + ".png", 0.1) for num in range(1, 3)]
dogJumpAnimation = PygAnimation([dogJumpImg[0]])
dogLandingAnimation = PygAnimation([dogJumpImg[1]])


# TODO refactoring and add speed
# TODO add a smile for Dog

class Dog(pygame.sprite.Sprite):
    containers = 0

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.animation = dogMoveAnimation
        self.size = (width, height)
        self.animation.scale(self.size)

        self.image = pygame.Surface(self.size)
        self.image.fill(BG_COLOR_SPRITE)
        self.image.set_colorkey(BG_COLOR_SPRITE)
        self.speed = 3
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.stages = ["Move", "Jump", "Landing"]
        self.stage = self.stages[0]
        self.animation.play()

    def update(self):
        self.image.fill(BG_COLOR_SPRITE)
        self.animation.blit(self.image, (0, 0))
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
                self.kill()

    def move(self):
        self.rect.x += self.speed

    def jump(self):
        self.rect.x += 4
        self.rect.y -= 8

    def landing(self):
        self.rect.x += 1
        self.rect.y += 8

    def getStage(self):
        return self.stage
