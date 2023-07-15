import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPACE = 10
    def __init__(self):
        # Tamaño de la nave
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT)) #
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS #
        self.rect.y = self.Y_POS
    
    def update(self, user_input):
        # Cuando se esconde la nave si se mueve hacia arriba o abajo, desaparece la nave
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()

    def move_left(self):
        self.rect.x -= self.SHIP_SPACE
        if self.rect.left == -SHIP_WIDTH: 
            self.rect.x = SCREEN_WIDTH
    
    def move_right(self):
        self.rect.x += self.SHIP_SPACE
        if self.rect.right == SCREEN_WIDTH + SHIP_WIDTH: 
            self.rect.x = -SHIP_WIDTH

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPACE

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.SHIP_SPACE

    def draw(self, screen):
        screen.blit(self.image, self.rect)