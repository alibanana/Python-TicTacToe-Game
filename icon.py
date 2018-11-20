import pygame

class Icon():
    def __init__(self, screen, status):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.status = status

        self.x_icon = pygame.image.load("images/x_icon.png")
        self.x_icon = pygame.transform.scale(self.x_icon, (80,80))
        self.x_icon_rect = self.x_icon.get_rect()

        self.o_icon = pygame.image.load("images/circle_icon.png")
        self.o_icon = pygame.transform.scale(self.o_icon, (80,80))
        self.o_icon_rect = self.o_icon.get_rect()
        
        self.icons_rect_data = []
        self.icons_rect_present_data = []

        y = -100
        for i in range(0, 3):
            y += 100
            x = 0
            for j in range(0, 3):
                temp = []
                temp.append(self.screen_rect.centerx - 140 + x)
                temp.append(self.screen_rect.centery - 140 + y)
                self.icons_rect_data.append(temp)
                x += 100

    def update(self, status):
        temp = []
        if status.pointer < len(self.icons_rect_data):
            a = self.icons_rect_data[status.pointer][0]
            b = self.icons_rect_data[status.pointer][1]
            temp.append(a)
            temp.append(b)
            if temp not in self.icons_rect_present_data and status.turn < 8:
                self.icons_rect_present_data.append(temp)
            elif temp not in self.icons_rect_present_data and status.turn >= 8:
                del self.icons_rect_present_data[0]
                self.icons_rect_present_data.append(temp)
            else:
                status.turn -= 1

    def draw_icons(self, status):
        pointer = 0
        for i in range (len(self.icons_rect_present_data)):
            a = self.icons_rect_present_data[pointer][0]
            b = self.icons_rect_present_data[pointer][1]
            if ((status.turn - len(self.icons_rect_present_data) + i) % 2) == 0:
                self.screen.blit(self.x_icon, (a,b))
            elif ((status.turn - len(self.icons_rect_present_data) + i) % 2) != 0:
                self.screen.blit(self.o_icon, (a,b))
            pointer += 1