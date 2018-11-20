import pygame

class Game_Screen():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.logo = pygame.image.load("images/TicTacToe_logo.png")
        self.logo = pygame.transform.scale(self.logo, (200, 40))
        self.logo_rect = self.logo.get_rect()

        self.logo_rect.left = 5
        self.logo_rect.top = 0

        #Square Settings
        self.square = pygame.image.load("images/square.png")
        self.square = pygame.transform.scale(self.square, (100,100))
        self.square_rect = self.square.get_rect()
        self.square_rect_data = []

        y = -100
        for i in range (0,3):
            y += 100
            x = 0
            for j in range (0,3):
                temp = []
                temp.append(self.screen_rect.centerx - 150 + x)
                temp.append(self.screen_rect.centery - 150 + y)
                self.square_rect_data.append(temp)
                x += 100

    def draw_game_screen(self):
        pointer = 0
        self.screen.blit(self.logo, self.logo_rect)
        for i in range(0,9):
            for j in range (0,1):
                a = self.square_rect_data[pointer][0]
                b = self.square_rect_data[pointer][1]
                self.screen.blit(self.square, (a,b))
            pointer += 1