import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, SHIELD_TYPE, SPACESHIP_TYPE


class BulletManager:
    def __init__(self):
        self.bullets: list[Bullet] = []
        self.enemy_bullets: list[Bullet] = []

    def update(self, game):
        
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
            if enemy_bullet.rect.colliderect(game.player.rect):
                    self.enemy_bullets.remove(enemy_bullet)
                    if game.player.power_up_type != SHIELD_TYPE:
                        game.playing = False
                        game.stats.death_count += 1
                        pygame.time.delay(1000)
                        break
        
        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    self.bullets.remove(bullet)
                    game.enemy_manager.enemies.remove(enemy)
                    game.stats.score += 1
                    break

        #for bullet, enemy in zip(self.bullets, game.enemy_manager.enemies):
            #bullet.update(self.bullets)
            #if bullet.rect.colliderect(enemy.rect):
                #self.bullets.remove(bullet)
                #game.enemy_manager.enemies.remove(enemy)
                #break

    def draw(self, screen):
        for bullet in self.enemy_bullets + self.bullets:
            bullet.draw(screen)

        #for bullet_enemy in self.enemy_bullets:
            #bullet_enemy.draw(screen)
        #for bullet in self.bullets:
            #bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
            #print(self.enemy_bullets)
        if bullet.owner == SPACESHIP_TYPE and not self.bullets:
            self.bullets.append(bullet)
            #print(self.bullets)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
