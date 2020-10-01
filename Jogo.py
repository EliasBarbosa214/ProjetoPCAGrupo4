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
fundo = pygame.image.load('Imagens/fundonovo.png')

# Object Grupo
objectGroup = pygame.sprite.Group()
redguyGroup = pygame.sprite.Group()
lixoGroup = pygame.sprite.Group()
shootGroup = pygame.sprite.Group()

guy = Guy(objectGroup)

#Timer

timer_relogio = 0
tempo_segundo = 0

font = pygame.font.SysFont('Arial Black', 50)
texto = font.render(':', True, (255, 255, 255))
pos_texto = texto.get_rect()
pos_texto.center = (40, 67)

#Pontos

tamanho = pygame.font.SysFont('Arial Black', 30)
pontos = 0
text = tamanho.render('Pontuação: ' + str(pontos), True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (430, 20)

#Jogo

display = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('Collectors')

# Music

#pygame.mixer.music.load('MusicSons/TownTheme.mp3')
#pygame.mixer.music.play(-1)

# Sounds

shoot = pygame.mixer.Sound('MusicSons/8bit_gunloop_explosion.wav')
colid = pygame.mixer.Sound('MusicSons/game-over2.wav')
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

        if (timer_relogio < 25):
            timer_relogio += 1

        else:
            tempo_segundo += 1
            texto = font.render(':' + str(tempo_segundo), True, (255, 255, 255))
            timer_relogio = 0

    #Update
        objectGroup.update()

        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.3:
                newRedGuy = RedGuy(objectGroup, redguyGroup)
                print('New Inimigo!')

        collision = pygame.sprite.spritecollide(guy, redguyGroup, False, pygame.sprite.collide_mask)

        if collision:
            print('Game OVER!')
            sair = False
            colid.play()

        timer += 1
        if timer > 30:
            if random.random() < 0.3:
                newLixo = Lixo(objectGroup, lixoGroup)
                print('New Lixo!')

        colect = pygame.sprite.spritecollide(guy, lixoGroup, True, pygame.sprite.collide_mask)


        if colect:
            print('Coletou')
            pontos = pontos + 1
            text = tamanho.render('Pontuação: ' + str(pontos), True, (255, 255, 255))
            coletou.play()

        if sair == False:
            print('Você terminou com total de: {} pontos.'.format(pontos))
            print('Você terminou com total de: {} segundos.'.format(tempo_segundo))


        #colect = pygame.sprite.spritecollide(lixoGroup, objectGroup, True)

    #Draw

        display.blit(fundo, (0,0)) #Background
        display.blit(texto, pos_texto)
        display.blit(text, textRect)
        objectGroup.draw(display)
        pygame.display.update()

pygame.quit()