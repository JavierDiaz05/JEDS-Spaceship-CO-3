
import pygame
from game.components.powerups.power_up import PowerUp
from game.utils.constants import SHIELD, SHIELD_TYPE


class Shield(PowerUp):
    def __init__(self):
        self.shield_image = pygame.transform.scale(SHIELD, (41, 41))
        super().__init__(self.shield_image, SHIELD_TYPE)
    
    