import pygame

class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (235,235,235)

    def play_sound(self, no):
        temp = "audio/button_clicked" + str(no) + ".wav"
        pygame.mixer.music.load(temp)
        pygame.mixer.music.play()