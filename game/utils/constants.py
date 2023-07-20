import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG_START = pygame.image.load(os.path.join(IMG_DIR, 'Other/bg_start.jpg'))
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMIES = [pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png")),
           pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png")),
           pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))]

SHIP_WIDTH = 40
SHIP_HEIGHT = 60

FONT_STYLE = 'freesansbold.ttf'
SCREEN_CENTER_W = SCREEN_WIDTH // 2
SCREEN_CENTER_H = SCREEN_HEIGHT // 2 
