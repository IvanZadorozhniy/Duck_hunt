
import pygame

from settings import BLACK, ORANGE, WHITE, WINDOW_HEIGHT, WINDOW_WIDHT, BLUE


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


def draw_start_menu(screen: pygame.Surface, surface_display: pygame.Surface, background_image: pygame.Surface):
    """
    Initializes Pygame and sets up the game window, background, and music.

    Returns:
    - screen_ (pygame.Surface): the game window surface
    - surface_display_ (pygame.Surface): a surface to display objects on before adding to the game window
    - background_ (pygame.Surface): the game background surface
    - background_music_ (pygame.mixer.Sound): the game background music
    """

    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('Duck Hunt', 200, bold=True)
    first_word_title = font.render('Duck', True, BLUE)
    second_word_title = font.render('Hunt', True, BLUE)
    pygame.draw.line(screen, ORANGE, (80, 190), (500, 190), 5)
    screen.blit(first_word_title, (80, 50))
    screen.blit(second_word_title, (160, 200))
    
    rect_start = pygame.draw.rect(screen,BLACK,(150, 400, 300, 60))
    rect_exit = pygame.draw.rect(screen,BLACK,(150, 480, 300, 60))

    font_menu_options = pygame.font.SysFont('Duck Hunt', 60, bold=False)
    start_game_option = font_menu_options.render("Start Game", True, WHITE)
    exit_game_option = font_menu_options.render("Exit Game", True, WHITE)
    screen.blit(start_game_option, (190, 410))
    screen.blit(exit_game_option, (190, 490))
    mousePos = pygame.mouse.get_pos()
    if rect_start.collidepoint(mousePos):
        pygame.draw.polygon(screen,WHITE,((170,425),(185,430), (170,435),(170,425)))
        
    if rect_exit.collidepoint(mousePos):
        pygame.draw.polygon(screen,WHITE,((170,505),(185,510), (170,515),(170,505)))
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mousePos):
                global game_state 
                game_state = "Game"
            if rect_exit.collidepoint(mousePos):
                pygame.quit()
                exit()
            

    pygame.display.update()


    
if __name__ == "__main__":
    screen, surface_display, background, background_music = set_up_pygame()
    from utils import game
    from utils import run_preview_of_game
    game_state = "Menu"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if game_state == "Menu":
            draw_start_menu(screen, surface_display, background)

        if game_state == "Game":
            run_preview_of_game(screen, surface_display, background)
            game(screen, surface_display, background)
