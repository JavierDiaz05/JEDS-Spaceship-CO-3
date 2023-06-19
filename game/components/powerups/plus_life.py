import pygame
from game.components.powerups.power_up import PowerUp
from game.utils.constants import PLUS_LIFE, PLUS_LIFE_TYPE


class PlusLife(PowerUp):
    def __init__(self):
        self.plus_life_image = pygame.transform.scale(PLUS_LIFE, (60, 41))
        super().__init__(self.plus_life_image, PLUS_LIFE_TYPE)
        #self.heart_image = pygame.transform.scale(PLUS_LIFE, (60, 41))
        self.heart_rect = self.plus_life_image.get_rect()
        self.heart_rect.y = 550
        self.heart_rect.x = 900