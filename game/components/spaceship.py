import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import DEFAULT_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, SPACESHIP, SPACESHIP_TYPE

class Spaceship(Sprite):
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500
        self.type = SPACESHIP_TYPE
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_up_time = 0
        self.hearts = []

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)
        
    def move_left(self):
        self.rect.x -= 10
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH -40

    def move_right(self):  
        self.rect.x += 10
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 50:
            self.rect.y += 10


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)

    def set_image(self, size=(60, 40), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def update_power_up(self, game):
        current_time = pygame.time.get_ticks()
        
        if self.power_up_time <= current_time and self.power_up_type != DEFAULT_TYPE:
            self.image = pygame.transform.scale(SPACESHIP, (60, 40))
            self.has_power_up = False
            self.power_up_type = DEFAULT_TYPE
            game.power_up_manager.reset()
        elif self.has_power_up == True:
            self.power_up_time -= 1
    
    def delet_heart(self):
        self.hearts.pop()

    def reset_hearts(self):
        self.hearts = []
