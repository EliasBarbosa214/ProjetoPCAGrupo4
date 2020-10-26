import pygame
import random

class Lixo2(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Imagens/jornal.png')
        #self.image = pygame.transform.scale(self.image, [60, 70])
        self.rect = pygame.Rect(60, 70, 60, 70)

        self.rect.x = random.randint(0, 890)
        self.rect.y = random.randint(120, 500)

        ############################################################

        if self.rect.top < 0:
            self.rect.top = 0

        elif self.rect.bottom > 650:
            self.rect.bottom = 680