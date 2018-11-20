import pygame
from settings import Settings as Settings
from start_menu import Start_Menu as start
from game_screen import Game_Screen as gamescreen
from game_status import GameStatus as gamestatus
from icon import Icon as Icon
from game_over_screen import Game_Over as gameover
import game_functions as func

def run_game():
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Tic Tac Toe")

    Start = start(screen)
    GameScreen = gamescreen(screen)
    status = gamestatus()
    icon = Icon(screen, status)
    GameOver = gameover(screen)

    func.update_screen(icon, ai_settings, screen, status, Start, GameScreen, GameOver)
    while True:
        func.check_events(icon, ai_settings, screen, status, Start, GameScreen, GameOver)

run_game()