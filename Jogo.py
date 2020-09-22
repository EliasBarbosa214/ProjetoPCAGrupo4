import pygame
from guy import Guy
from redGuy import RedGuy
from lixo import Lixo
import random

try:
    pygame.init()
except:
    print('O módulo pygame não foi inicializado com sucesso')

largura = 940
altura = 600
relogio = pygame.time.Clock()
fundo = pygame.image.load('Imagens/fundo2d.jpg')

# Object Grupo
objectGroup = pygame.sprite.Group()
redguyGroup = pygame.sprite.Group()
lixoGroup = pygame.sprite.Group()

guy = Guy(objectGroup)




#

display = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('Collectors')

# Music

pygame.mixer.music.load('MusicSons/TownTheme.mp3')
pygame.mixer.music.play(-1)

# Sounds
shoot = pygame.mixer.Sound('MusicSons/8bit_gunloop_explosion.wav')
colid = pygame.mixer.Sound('MusicSons/game over2.wav')
coletou = pygame.mixer.Sound('MusicSons/appear-online.ogg')

#Teclas

sair = True
clock = pygame.time.Clock()
timer = 20
if __name__ == "__main__":
    while sair:
        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot.play()



    #Update
        objectGroup.update()

        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.3:
                newRedGuy = RedGuy(objectGroup, redguyGroup)
                print('New Inimigo!')

        collision = pygame.sprite.spritecollide(guy, redguyGroup, False)

        if collision:
            print('Game OVER!')
            sair = False
            colid.play()

        timer += 1
        if timer > 30:
            if random.random() < 0.3:
                newLixo = Lixo(objectGroup, lixoGroup)
                print('New Lixo!')

        colect = pygame.sprite.spritecollide(guy, lixoGroup, True)

        if colect:
            print('Coletou')
            coletou.play()

        #colect = pygame.sprite.spritecollide(lixoGroup, objectGroup, True)

    #Draw

        display.blit(fundo, (0,0)) #Background
        objectGroup.draw(display)
        pygame.display.update()

pygame.quit()