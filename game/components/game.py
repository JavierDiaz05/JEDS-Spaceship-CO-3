
from game.components.bullets.bullet_manager import BulletManager
import pygame
from game.components.enemies.enemy_manager import EnemyManger
from game.components.menu import Menu
from game.components.powerups.power_up_manager import PowerUpManager
from game.components.spaceship import Spaceship
from game.components.stats import Stats

from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.death_count = 0

        self.player = Spaceship()
        self.enemy_manager = EnemyManger()
        self.bullet_manager = BulletManager()
        self.stats = Stats()
        self.menu = Menu("Press any key to start...", self.stats)
        self.power_up_manager = PowerUpManager()


    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def play(self):
        self.enemy_manager.reset()
        self.stats.score = 0
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running =False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        self.player.update_power_up(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.draw_power_up_time()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.stats.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)
    
    def draw_power_up_time(self):
        current_time = pygame.time.get_ticks()
        if self.player.power_up_time == 0 or self.player.power_up_time <= current_time:
            time = 0
        else:
            time = (self.player.power_up_time - current_time) // 1000
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Power up: {time}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (100, 50)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        if self.stats.death_count > 0:
            self.stats.update()
            self.menu.update_message("Press any key to try again...", self.stats)

        self.menu.draw(self.screen, self.stats)
        self.menu.events(self.on_close, self.play)

    def on_close(self):
        self.playing = False
        self.running = False

    def reset(self):
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.power_up_manager.reset()
        self.power_up_manager.reset()



