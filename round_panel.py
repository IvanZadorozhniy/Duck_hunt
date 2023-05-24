import pygame

from settings import BLACK, GREEN, RED

PATH_DUCK_ICON = 'images/duck_icon.png'
SIZE_PANEL = (300, 50)
SIZE_ICON = (15, 15)
POSITION_PANEL = (140, 515)
HORIZONTAL_POSITION_DUCK_ICON = 2
MAX_DUCKS = 10


class RoundPanel(pygame.sprite.Sprite):
    containers = pygame.sprite.RenderUpdates()

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.size = SIZE_PANEL
        self.image = pygame.Surface(self.size)
        self.duck_icon = pygame.image.load(PATH_DUCK_ICON)
        self.duck_icon = pygame.transform.scale(self.duck_icon, SIZE_ICON)
        self.success_duck_icon = change_color(self.duck_icon, GREEN)
        self.fail_duck_icon = change_color(self.duck_icon, RED)
        self.attempts = []
        self.rect = self.image.get_rect()
        self.rect.x = POSITION_PANEL[0]
        self.rect.y = POSITION_PANEL[1]

    def update(self):
        self.image.blit(self.duck_icon, (100, 2))
        for i, attempt in enumerate(self.attempts):
            chooosen_icon = self.success_duck_icon if attempt else self.fail_duck_icon
            self.image.blit(
                chooosen_icon, (20+20*i, HORIZONTAL_POSITION_DUCK_ICON))
        for i in range(len(self.attempts), MAX_DUCKS):
            self.image.blit(
                self.duck_icon, (20+20*i, HORIZONTAL_POSITION_DUCK_ICON))

    def add_attempt(self, is_succes):
        self.attempts.append(is_succes)

    def clean_panel(self):
        self.attempts.clear()

    @staticmethod
    def draw_background(surface):
        pygame.draw.rect(surface, 
                         BLACK, 
                         (POSITION_PANEL[0], POSITION_PANEL[1], SIZE_PANEL[0], SIZE_PANEL[1]),
                         )


def change_color(image, color):
    coloured_image = pygame.Surface(image.get_size())
    coloured_image.fill(color)

    final_image = image.copy()
    final_image.blit(coloured_image, (0, 0), special_flags=pygame.BLEND_MULT)
    return final_image
