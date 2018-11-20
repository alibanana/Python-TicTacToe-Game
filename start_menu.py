import pygame

class Start_Menu():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.logo = pygame.image.load("images/TicTacToe_logo.png")
        self.logo = pygame.transform.scale(self.logo,(200,40))
        self.logo_rect = self.logo.get_rect()

        self.start = pygame.image.load("images/start_button.png")
        self.start = pygame.transform.scale(self.start,(250,120))
        self.start_rect = self.start.get_rect()

        self.quit = pygame.image.load("images/quit_button.png")
        self.quit = pygame.transform.scale(self.quit,(160,80))
        self.quit_rect = self.quit.get_rect()

        self.logo_rect.left = 5
        self.logo_rect.top = 0
        self.start_rect.centerx = self.screen_rect.centerx
        self.start_rect.centery = self.screen_rect.centery
        self.quit_rect.centerx = self.screen_rect.centerx
        self.quit_rect.bottom = 580

    def draw_start(self):
        self.screen.blit(self.logo, self.logo_rect)
        self.screen.blit(self.start, self.start_rect)
        self.screen.blit(self.quit, self.quit_rect)