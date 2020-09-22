import pygame
import random

class RedGuy(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Imagens/monstro.png')
        self.image = pygame.transform.scale(self.image, [60, 55])
        self.rect = pygame.Rect(60, 55, 60, 55)
        self.rect.x = 940 + random.randint(1 , 400)
        self.rect.y = random.randint(2, 550)
        self.speed = 3 + random.random() * 2


    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
