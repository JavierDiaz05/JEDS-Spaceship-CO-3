import pygame
from game.utils.constants import BG, FONT_STYLE, GAME_OVER, ICON, PLAY, RESET, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

    def __init__(self, message_stats, text_size=30):
        self.font = pygame.font.Font(FONT_STYLE, text_size)
        self.icon = pygame.transform.scale(ICON, (120, 80))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)

        self.background = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_rect = self.background.get_rect()
        self.background_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

        self.play_button = pygame.transform.scale(PLAY, (90, 90))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 120)

        self.reset_button = pygame.transform.scale(RESET, (75, 101))
        self.reset_button_rect = self.reset_button.get_rect()
        self.reset_button_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 120)

        self.game_over = pygame.transform.scale(GAME_OVER, (386, 40))
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)

        self.update_message( message_stats)


    def events(self, on_close, on_start):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.play_button_rect.collidepoint(mouse_pos):
                    on_start()
        
        
        #mouse_click = pygame.mouse.get_pressed()
        #if self.play_button_rect.collidepoint(mouse_pos) and mouse_click[0] == 1 or self.reset_button_rect.collidepoint(mouse_pos) and mouse_click[0] == 1:
            #on_start()

    def draw(self, screen, stats):
        screen.blit(self.background, self.background_rect)
        if stats.death_count > 0:
            #screen.fill((255, 255, 255))
            screen.blit(self.text_stats, self.text_stats_rect)
            screen.blit(self.game_over, self.game_over_rect)
            screen.blit(self.reset_button, self.reset_button_rect)
        else:
            #screen.fill((255, 255, 255))
            screen.blit(self.play_button, self.play_button_rect)
            screen.blit(self.icon, (self.icon_rect))
        pygame.display.update()

    def update_message(self, message_stats):

        self.message_stats = message_stats.update_message()
        self.text_stats = self.font.render(self.message_stats, True, (255, 255, 255))
        self.text_stats_rect = self.text_stats.get_rect()
        self.text_stats_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)


