
import pygame

from settings import WINDOW_HEIGHT, WINDOW_WIDHT


def set_up_pygame():
    """
    Initializes Pygame and sets up the game window, background, and music.

    Returns:
    - screen_ (pygame.Surface): the game window surface
    - surface_display_ (pygame.Surface): a surface to display objects on before 
      adding to the game window
    - background_ (pygame.Surface): the game background surface
    - background_music_ (pygame.mixer.Sound): the game background music
    """
    pygame.init()
    pygame.font.init()
    size = [WINDOW_HEIGHT, WINDOW_WIDHT]
    screen_ = pygame.display.set_mode(size)

    background_ = pygame.image.load("images//background.png").convert()
    background_ = pygame.transform.scale(background_, screen_.get_size())
    background_.set_colorkey(background_.get_at((0, 0)))

    surface_display_ = pygame.Surface(screen_.get_size())

    pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=2**6)
    background_music_ = pygame.mixer.Sound("music//8-bit.ogg")
    background_music_.set_volume(0.3)

    background_music_.play(-1)
    return screen_, surface_display_, background_, background_music_


if __name__ == "__main__":
    screen, surface_display, background, background_music = set_up_pygame()
    from utils import game
    from utils import run_preview_of_game
    if pygame.display.get_init():
        run_preview_of_game(screen, surface_display, background)

    if pygame.display.get_init():
        game(screen, surface_display, background)
