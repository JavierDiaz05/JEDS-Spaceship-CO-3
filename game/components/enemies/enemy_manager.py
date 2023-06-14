from game.components.enemies.enemy import Enemy
from game.components.enemies.new_enemy import NewEnemy


class EnemyManger:
    def __init__(self):
        self.enemies: list[Enemy] = []

    def update(self):
        if not self.enemies:
            self.enemies.append(Enemy())
            self.enemies.append(NewEnemy())
        
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

