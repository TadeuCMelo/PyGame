import sys
import pygame
from settings import Settings

class RebentaBalans:
    """Classe principal do jogo para gerir os comportamentos e recursos do jogo"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 

        self.bg_color = self.settings.bg_color
        pygame.display.set_caption(self.settings.screen_caption)

    def run_game(self):
        while True:
            """ Verificar eventos de teclado e rato """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        # Redesenha o ecrã a cada passagem pelo loop
        self.screen.fill(self.bg_color)
        self.background.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Cirar o nosso objeto do jogo e iniciar o loop principal
    rb = RebentaBalans()
    rb.run_game()
