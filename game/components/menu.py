import pygame
from game.utils.constants import FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

    def __init__(self, message, message_stats, text_size=30):
        self.font = pygame.font.Font(FONT_STYLE, text_size)
        self.icon = pygame.transform.scale(ICON, (120, 80))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        self.update_message(message, message_stats)


    def events(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.KEYDOWN:
                on_start()

    def draw(self, screen, stats):
        if stats.death_count > 0:
            screen.fill((255, 255, 255))
            screen.blit(self.text_stats, self.text_stats_rect)
            screen.blit(self.text_game_over, self.text_game_over_rect)
            screen.blit(self.text, self.text_rect)
        else:
            screen.fill((255, 255, 255))
            screen.blit(self.icon, (self.icon_rect))
            screen.blit(self.text, self.text_rect)
        pygame.display.update()

    def update_message(self, message, message_stats):
        self.message = message
        self.text = self.font.render(self.message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

        self.message_stats = message_stats.update_message()
        self.text_stats = self.font.render(self.message_stats, True, (0, 0, 0))
        self.text_stats_rect = self.text_stats.get_rect()
        self.text_stats_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 80)

        self.message_game_over = "GAME OVER"
        self.text_game_over = self.font.render(self.message_game_over, True, (244, 0, 0))
        self.text_game_over_rect = self.text_game_over.get_rect()
        self.text_game_over_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
    
