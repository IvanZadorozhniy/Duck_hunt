import pygame

from settings import BLACK, GREEN, RED



class RoundPanel(pygame.sprite.Sprite):
    containers = pygame.sprite.RenderUpdates()

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.size = (300, 50)
        self.image = pygame.Surface(self.size)
        
        self.duck_icon = pygame.image.load('images/duck_icon.png')
        self.duck_icon = pygame.transform.scale(self.duck_icon, (15, 15))
        
        self.success_duck_icon = change_color(self.duck_icon, GREEN)
        self.fail_duck_icon = change_color(self.duck_icon, RED)
        
        self.attempts = []
        self.rect = self.image.get_rect()
        self.rect.x = 140
        self.rect.y = 515

    def update(self):
        self.image.fill(BLACK)
        self.image.blit(self.duck_icon, (100, 2))
        for i,attempt in enumerate(self.attempts):
            self.image.blit(self.success_duck_icon if attempt else self.fail_duck_icon, (20+20*i, 2))
              
        for i in range(len(self.attempts), 10):
            self.image.blit(self.duck_icon, (20+20*i, 2))
    
    def add_attempt(self, is_succes):
        self.attempts.append(is_succes)
    
    def clean_panel(self):
        self.attempts.clear()

def change_color(image, color):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(color)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage