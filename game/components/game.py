import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, ICON, FONT_STYLE, SCREEN_CENTER_H
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.running = False
        self.menu = Menu('Press any key to start ...', self.screen)
        self.score = 0
        self.death_count = 0
        self.high_score = []

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)

        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            
            self.menu.update_message("Game Over")
            self.menu.draw(self.screen)
            self.menu.update_message(f"Score: {self.score_screen}", SCREEN_CENTER_H + 40)
            self.menu.draw(self.screen)
            self.menu.update_message(f"High Score: {self.high_score_screen}", SCREEN_CENTER_H + 80)
            self.menu.draw(self.screen)
            self.menu.update_message(f"Deaths: {self.death_count}", SCREEN_CENTER_H + 120)
            self.menu.draw(self.screen)

        icon = self.image = pygame.transform.scale(ICON, (80, 120))
        self.screen.blit(icon, ((SCREEN_WIDTH // 2) - 40, (SCREEN_HEIGHT // 2) - 150))
        self.menu.update(self)

    def draw_score(self):
        self.score_screen = self.score
        self.high_score.append(self.score_screen)
        self.high_score_screen = max(self.high_score)
        if self.playing == False:
            self.score = 0
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score_screen}', True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

