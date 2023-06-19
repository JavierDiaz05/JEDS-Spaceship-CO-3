import random
from game.components.enemies.enemy import Enemy


class EnemyManger:
    def __init__(self):
        self.enemies: list[Enemy] = []
        self.difficult = 2
        self.level_up = 3

    def update(self, game):
        if not self.enemies:
            if game.stats.score == self.level_up:
                while len(self.enemies) < self.difficult:
                    enemy_variant = random.randint(1, 3)
                    self.enemies.append(Enemy(enemy_variant))
                self.level_up += 3
                self.difficult += 1
            else:
                enemy_variant = random.randint(1, 3)
                self.enemies.append(Enemy(enemy_variant))
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def reset(self):
        self.enemies = []
        self.difficult = 2
        self.level_up = 3

