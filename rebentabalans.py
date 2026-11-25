import sys
import pygame
from settings import Settings
from porco_espim import Player

class RebentaBalans:
    """Classe principal do jogo para gerir os comportamentos e recursos do jogo"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) 

        self.porcoespim = Player(self)

        self.bg_color = self.settings.bg_color
        pygame.display.set_caption(self.settings.screen_caption)


    def run_game(self):
        while True:
            self._update_screen()
            self.porcoespim.update()
            self._check_events()


    def _check_events(self):
        """ Verificar eventos de teclado e rato """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """responder aos eventos de keydown"""
        if event.key == pygame.K_RIGHT:
            #vai mexer pa direita
            self.porcoespim.movendo_direita = True
        elif event.key == pygame.K_LEFT:
            #vai mexer pa esquerda
            self.porcoespim.movendo_esquerda = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.porcoespim.movendo_direita = False
        if event.key == pygame.K_LEFT:
            self.porcoespim.movendo_esquerda = False
    
    
    def _update_screen(self):
        # Redesenha o ecrã a cada passagem pelo loop
        self.screen.fill(self.bg_color)
        self.porcoespim.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Cirar o nosso objeto do jogo e iniciar o loop principal
    rb = RebentaBalans()
    rb.run_game()
