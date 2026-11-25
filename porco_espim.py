import pygame

class Player:
    """Classe para gerir o porco espim"""

    def __init__(self,rb_game):
        """Inicializar o porco espim e posiçao pa começar"""
        self.screen = rb_game.screen
        self.settings = rb_game.settings
        self.screen_rect = rb_game.screen.get_rect()

        #Controlo de movimento do porco espim
        self.movendo_direita = False
        self.movendo_esquerda = False

        #carregar a imagem do porco espim
        self.image = pygame.image.load('images/porcoespim.png')
        self.rect = self.image.get_rect()

        #definir posiçao inicial do porco espim

        self.rect.midbottom = self.screen_rect.midbottom

        #Guarda a posição X e Y do porco espim

        self.x = float (self.rect.x)


    def update(self):
        #atualiza a posição do porco espim
        if self.movendo_direita and self.rect.right < self.screen_rect.right:
            self.x += self.settings.porcoespim_speed
        if self.movendo_esquerda and self.rect.left > 0:
            self.x -= self.settings.porcoespim_speed

        self.rect.x = self.x

    def blitme(self):
        #desenha a nave na posiçao atual
        self.screen.blit(self.image, self.rect)
