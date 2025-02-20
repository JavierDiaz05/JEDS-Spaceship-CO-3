from game.components.bullets.bullet import Bullet
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
import random

LEFT = 'left'
RIGHT = 'right'
IMAGE = 'image'
SPEED_X = 'speed_x'
SPEED_Y = 'speed_y'
MOVE_X = 'move_x'

class Enemy(Sprite):
    MOVEMENTS = ['LEFT', 'RIGHT']
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050]
    Y_POS = -1
    VARIANTS = {
        1:{
            IMAGE: ENEMY_1,
            SPEED_X: 5,
            SPEED_Y: 1,
            MOVE_X: (30, 100)
        },
        2:{
            IMAGE: ENEMY_2,
            SPEED_X: 5,
            SPEED_Y: 2,
            MOVE_X: (50, 120)
        },
        3:{
            IMAGE: ENEMY_3,
            SPEED_X: 0,
            SPEED_Y: 20,
            MOVE_X: (0, 0)
        }
    }

    def __init__(self, variant):
        self.enemy_variant = self.VARIANTS[variant]
        self.image = pygame.transform.scale(self.enemy_variant[IMAGE], (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE

        self.speed_x = self.enemy_variant[SPEED_X]
        self.speed_y = self.enemy_variant[SPEED_Y]

        self.movement = random.choice(self.MOVEMENTS)
        lower_limit, upper_limit = self.enemy_variant[MOVE_X]
        self.move_x = random.randint(lower_limit, upper_limit)
        self.moving_index = 0
        self.shooting_time = int(pygame.time.get_ticks() // 1000) + random.randint(1, 2)
        

    def update(self, ships, game):
        self.rect.y += self.speed_y
        if self.enemy_variant[IMAGE] != ENEMY_3:
            self.shoot(game)

        if self.movement == LEFT:
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        
        self.update_movement()
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
        
        if self.enemy_variant[IMAGE] == ENEMY_3:
            if self.rect.colliderect(game.player.rect):
                if len(game.player.hearts) > 0:
                        game.player.delet_heart()
                else:
                    game.playing = False
                    game.stats.death_count += 1
                    pygame.time.delay(1000)
                game.enemy_manager.enemies.remove(self)

    def update_movement(self):
        self.moving_index += 1
        if self.rect.x >= SCREEN_WIDTH - 50:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement = RIGHT
        
        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, game):
        current_time = int(pygame.time.get_ticks() // 1000)

    
        if  current_time == self.shooting_time:
            bullet = Bullet(self)
            game.bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(1, 2)
