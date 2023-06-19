import pygame
import random
from game.components.powerups.plus_life import PlusLife
from game.components.powerups.shield import Shield
from game.utils.constants import PLUS_LIFE_TYPE, SHIELD_TYPE, SPACESHIP_SHIELD, SPACESHIP_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 10000
        self.duration = 5000

    def add_power_up(self):
        self.random_power_up = random.randint(1, 3)
        if self.random_power_up == 1:
            power_up = Shield()
            self.power_ups.append(power_up)
        elif self.random_power_up == 2:
            power_up = PlusLife()
            self.power_ups.append(power_up)
        else:
            pass
        
        


    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears and game.player.has_power_up == False:
            self.add_power_up()
            self.when_appears += 10000


        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                if game.player.power_up_type == SHIELD_TYPE:
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    game.player.power_up_time = power_up.start_time + self.duration
                elif game.player.power_up_type == PLUS_LIFE_TYPE:
                    if len(game.player.hearts) < 3:
                        game.player.hearts.append(power_up)
                    if len(game.player.hearts) > 1:
                        power_up.heart_rect.x = game.player.hearts[len(game.player.hearts) - 2].heart_rect.x + 50
                self.power_ups.remove(power_up)
                


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)


    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = now + 10000