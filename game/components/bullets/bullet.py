from pygame.sprite import Sprite
import pygame

from game.utils.constants import BULLET, BULLET_ENEMY, ENEMY_TYPE, SCREEN_HEIGHT

IMAGE = 'image'
OWNER = 'owner'
class Bullet(Sprite):
    SPEED = 20
    #ENEMY_BULLET_IMG = pygame.transform.scale(BULLET_ENEMY, (9, 32))
    #BULLETS = {ENEMY_TYPE: ENEMY_BULLET_IMG}
    VARIANTS = {
        1:{
            IMAGE: BULLET_ENEMY
        },
        2:{
            IMAGE: BULLET
        }
    }

    def __init__(self, spaceship):
        if spaceship.type == ENEMY_TYPE:
            bullet_variant = self.VARIANTS[1]
        else:
            bullet_variant = self.VARIANTS[2]
        self.image = pygame.transform.scale(bullet_variant[IMAGE], (9, 32))
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type

    def update(self, bullets):
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)
        else:
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))