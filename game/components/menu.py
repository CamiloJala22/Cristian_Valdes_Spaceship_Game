import pygame
from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_CENTER_H, SCREEN_CENTER_W, BG_START, BG_GAME_OVER

class Menu:
    def __init__(self, screen):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        # self.text = self.font.render(message, True, (0, 0, 0))
        # self.text_rect = self.text.get_rect()
        # self.text_rect.center = (SCREEN_CENTER_W, SCREEN_CENTER_H)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen, message, x = SCREEN_CENTER_W, y = SCREEN_CENTER_H, color = (0, 0, 0)):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_CENTER_W, y)
        screen.blit(text, text_rect)


    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game.run()

    def reset_screen_color(self, screen):
        image = pygame.transform.scale(BG_START, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(image, (0,0))

    def death_screen(self, screen):
        screen.blit(BG_GAME_OVER, (SCREEN_CENTER_W - 193, SCREEN_CENTER_H - 20))

    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (SCREEN_CENTER_W, SCREEN_CENTER_H)