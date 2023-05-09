
import pygame

from settings import WINDOW_HEIGHT, WINDOW_WIDHT



def set_up_pygame():
    pygame.init()
    pygame.font.init()
    size = [WINDOW_HEIGHT, WINDOW_WIDHT]
    screen = pygame.display.set_mode(size)

    background = pygame.image.load("images//background.png").convert()
    background = pygame.transform.scale(background, screen.get_size())
    background.set_colorkey(background.get_at((0, 0)))

    surface_display = pygame.Surface(screen.get_size())

    pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=2**6)
    background_music = pygame.mixer.Sound("music//8-bit.ogg")
    background_music.set_volume(0.3)

    background_music.play(-1)
    return screen, surface_display, background, background_music


if __name__ == "__main__":
    screen, surface_display, background, background_music = set_up_pygame()
    from utils import game
    from utils import run_preview_of_game
    # if pygame.display.get_init():
    #     run_preview_of_game(screen, surface_display, background)

    if pygame.display.get_init():
        game(screen, surface_display, background)
