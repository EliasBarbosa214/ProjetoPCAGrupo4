import pygame
import math

class Guy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Imagens/monstro2.png')
        self.image = pygame.transform.scale(self.image, [40, 70])
        self.rect = pygame.Rect(40, 70, 40, 70)

    def update(self, *args):
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and pos_x <= 870:
            self.rect.x += 40
        if comandos[pygame.K_LEFT]: # and pos_x <= 870:
            self.rect.x -= 40
        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 40
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 40

############################################################


        if self.rect.top < 0:
            self.rect.top = 0

        elif self.rect.bottom > 650:
            self.rect.bottom = 680