import pygame

from settings import BLACK, NUM_BULLETS, WHITE

PATH_BULLET_SPRITE = 'images/bullet.png'
SIZE_BULLET = (10, 25)
FONT_SIZE = 25
FONT_NAME = 'Duck Hunt'
SIZE_PANEL = (65, 50)
POSITION_PANEL = (50,515)
POSITION_TEXT = (10, 30)
INTEND_BULLET = 13
STEP_BETWEEN_BULLET = 15
HORIZONTAL_POSTION_BULLET = 2

def get_position_bullet(num_bullet):
    return (INTEND_BULLET+STEP_BETWEEN_BULLET*num_bullet, HORIZONTAL_POSTION_BULLET)

class BulletPanel(pygame.sprite.Sprite):
    containers = pygame.sprite.RenderUpdates()

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.size = SIZE_PANEL
        self.image = pygame.Surface(self.size)

        self.myfont = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

        self.surface_shot = self.myfont.render("SHOT", False, WHITE)

        self.bullet_surface = pygame.image.load(PATH_BULLET_SPRITE)
        self.bullet_surface = pygame.transform.scale(
            self.bullet_surface, SIZE_BULLET)

        self.bullets = NUM_BULLETS

        self.rect = self.image.get_rect()
        self.rect.x = POSITION_PANEL[0]
        self.rect.y = POSITION_PANEL[1]

    def update(self):
        
        self.image.blit(self.surface_shot, POSITION_TEXT)
        for num_bullet in range(self.bullets):
            self.image.blit(self.bullet_surface, get_position_bullet(num_bullet))

    def set_bullets(self, bullets):
        """
        Sets the bullets of the object to the given list of bullets.

        Args:
            bullets (list): A list of bullet objects representing the bullets of the object.
        """

        self.bullets = bullets
    
    @staticmethod
    def draw_background(surface):
        pygame.draw.rect(surface, 
                         BLACK, 
                         (POSITION_PANEL[0], POSITION_PANEL[1], SIZE_PANEL[0], SIZE_PANEL[1]),
                         )