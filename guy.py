import pygame

class Guy(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('data/Imagens/personagem4.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 450
        self.rect.y = 300

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 30
            self.image = pygame.image.load('data/Imagens/lado1.png')
            self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 30
            self.image = pygame.image.load('data/Imagens/lado2.png')
            self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 30
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 30

        if self.rect.right < 40:
            self.rect.right = 40

        if self.rect.left > 895:
            self.rect.left = 895


        def get_frame_by_gid(gid):
            global sprite_sheet
            columns = 9
            width = 64
            height = 64
            space_h = 0
            margin = 0
            top = 0
            space_v = 0
            linha = gid // columns
            coluna = gid % columns
            x = (coluna * (width + space_h)) + margin
            y = (linha * (height + space_v)) + top
            quadro = sprite_sheet.subsurface(pygame.Rect((x, y), (width, height)))
            return quadro


############################################################

        if self.rect.top <= 120:
            self.rect.top = 120

        elif self.rect.bottom > 600:
            self.rect.bottom = 600

'''elif self.rect.right <= 600:
            self.rect.right = 600

        elif self.rect.left >= 20:
            self.rect.left = 20'''

