from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy = Enemy()
            self.enemies.append(enemy)