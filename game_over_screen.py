import pygame

class Game_Over():
	def __init__(self, screen):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		self.game_over_icon = pygame.image.load("images/game_over_icon.png")
		self.game_over_icon = pygame.transform.scale(self.game_over_icon,(400,300))
		self.game_over_icon_rect = self.game_over_icon.get_rect()

		self.player_1_wins_icon = pygame.image.load("images/player_1_wins.png")
		self.player_1_wins_icon = pygame.transform.scale(self.player_1_wins_icon,(600,150))
		self.player_1_wins_icon_rect = self.player_1_wins_icon.get_rect()
		self.player_2_wins_icon = pygame.image.load("images/player_2_wins.png")
		self.player_2_wins_icon = pygame.transform.scale(self.player_2_wins_icon,(600,150))
		self.player_2_wins_icon_rect = self.player_2_wins_icon.get_rect()

		self.game_over_icon_rect.centerx = self.screen_rect.centerx
		self.game_over_icon_rect.centery = self.screen_rect.centery + 30
		self.player_1_wins_icon_rect.centerx = self.screen_rect.centerx
		self.player_1_wins_icon_rect.centery = self.game_over_icon_rect.top - 30
		self.player_2_wins_icon_rect.centerx = self.screen_rect.centerx
		self.player_2_wins_icon_rect.centery = self.game_over_icon_rect.top - 30

	def draw_game_over_screen(self, status, icon):
		self.screen.blit(self.game_over_icon, self.game_over_icon_rect)
		if status.turn % 2 == 0:
			self.screen.blit(self.player_1_wins_icon, self.player_1_wins_icon_rect)
		elif status.turn % 2 != 0:
			self.screen.blit(self.player_2_wins_icon, self.player_2_wins_icon_rect)