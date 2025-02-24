import pygame
from random import randint
from pygame.sprite import Sprite
from game.utils.constants import ENEMIES, SHIP_WIDTH, SHIP_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    Y_POS = 20
    SPEED_X = randint(5, 10)
    SPEED_Y = randint(1, 5)
    MOV_X = {0: 'left', 1: 'right'}
    def __init__(self):
        self.image = ENEMIES[randint(0, 2)]
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, SCREEN_WIDTH // 2)
        self.rect.y = self.Y_POS

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOV_X[randint(0, 1)]
        self.move_x_for = randint(0, SCREEN_WIDTH)
        self.step = 0
        self.type = 'enemy'
        self.shooting_time = randint(50, 500)

    def update(self, enemies, game):
        self.rect.y += self.speed_y
        current_time = pygame.time.get_ticks()
        if current_time >= self.shooting_time:
            self.shoot(game.bullet_manager)
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)

    def shoot(self, bullet_manager):
            bullet = Bullet(self)
            self.shooting_time += randint(100, 1000)
            bullet_manager.add_bullet(bullet)
            


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def change_movement_x(self):
        self.step += 1 
        if (self.step >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - SHIP_WIDTH):
            self.movement_x = 'left'
            self.step = 0
        if (self.step >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.step = 0