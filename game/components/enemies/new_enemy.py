import random
import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2


class NewEnemy(Enemy):
    SPEED_Y = 15
    SPEED_X = 0

    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_2, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS

        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X

        self.movement = random.choice(self.MOVEMENTS)
        self.move_x = random.randint(30, 100)
        self.moving_index = 0
