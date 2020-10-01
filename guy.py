import pygame


class Guy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Imagens/personagem3.png')
        self.image = pygame.transform.scale(self.image, [55, 85])
        self.rect = pygame.Rect(50, 80, 50, 80)

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

        elif self.rect.bottom > 600:
            self.rect.bottom = 600

'''
w = 50
h = 85
win = pygame.display.set_mode((w, h))
img = pygame.image.load()

        def maske_blit(fundo, img, wx, wy, x, y, w, h):
            Surf = pygame.SUrface((w, h)).convert()
            Surf.blit(img, (0,0), (wx,wy,w,h))
            alpha = Surf.get_at(0,0)
            Surf.set_colorkey(alpha)
            win.blit(Surf, (200, 200))
'''