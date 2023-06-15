import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, SPACESHIP_TYPE


class BulletManager:
    def __init__(self):
        self.bullets: list[Bullet] = []
        self.enemy_bullets: list[Bullet] = []

    def update(self, game):
        for enemy_bullet, bullet, enemy  in zip(self.enemy_bullets, self.bullets, game.enemy_manager.enemies):
            enemy_bullet.update(self.enemy_bullets)
            bullet.update(self.bullets)
            if enemy_bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(enemy_bullet)
                game.playing = False
                pygame.time.delay(1000)
                break
            elif bullet.rect.colliderect(enemy.rect):
                self.bullets.remove(bullet)
                game.enemy_manager.enemies.remove(enemy)
                break

        #for bullet, enemy in zip(self.bullets, game.enemy_manager.enemies):
            #bullet.update(self.bullets)
            #if bullet.rect.colliderect(enemy.rect):
                #self.bullets.remove(bullet)
                #game.enemy_manager.enemies.remove(enemy)
                #break

    def draw(self, screen):
        for bullet_enemy, bullet in zip(self.enemy_bullets, self.bullets):
            bullet_enemy.draw(screen)
            bullet.draw(screen)

        #for bullet_enemy in self.enemy_bullets:
            #bullet_enemy.draw(screen)
        #for bullet in self.bullets:
            #bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
            #print(self.enemy_bullets)
        elif bullet.owner == SPACESHIP_TYPE and not self.bullets:
            self.bullets.append(bullet)
            #print(self.bullets)