import os, sys

import pygame
from guy import Guy
from lixo2 import Lixo2
from redGuy import RedGuy
from lixo import Lixo
import random

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

####

pygame.init()
WIDTH = 940
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#titulo = pygame.image.load("Imagens/fundomenu.png")
jogarp = pygame.image.load("data/Imagens/jogarmarrom.png")
jogarb = pygame.image.load("data/Imagens/jogarbranco.png")
sairp = pygame.image.load("data/Imagens/SAIRp.png")
sairb = pygame.image.load("data/Imagens/SAIR.png")
fundo = pygame.image.load("data/Imagens/fundomenu2.png")
creditob = pygame.image.load('data/Imagens/credito.png')
creditop = pygame.image.load('data/Imagens/creditop.png')


gameover = pygame.image.load('data/Imagens/testegame2.png')
umaEstrela = pygame.image.load('data/Imagens/1estrela.png')
duasEstrelas = pygame.image.load('data/Imagens/2estrela.png')
tresEstrelas = pygame.image.load('data/Imagens/3estrela.png')


pygame.mixer.music.load('data/MusicSons/sons/musica de fundo/menu.mp3')
pygame.mixer.music.play(-1)

def Jogo():
    largura = 940
    altura = 600
    fundojogo = pygame.image.load('data/Imagens/cidade2.jpg')
    # fundojogo = pygame.transform.scale(fundojogo, [940, 600])

    # Object Grupo
    objectGroup = pygame.sprite.Group()
    redguyGroup = pygame.sprite.Group()
    lixoGroup = pygame.sprite.Group()
    shootGroup = pygame.sprite.Group()
    lixoGroup2 = pygame.sprite.Group()

    guy = Guy(objectGroup)

    pygame.mixer.music.load('data/MusicSons/sons/musica de fundo/menu.mp3')
    pygame.mixer.music.play(-1)

    # Timer
    timer_relogio = 0
    tempo_segundo = 0

    font = pygame.font.SysFont('Arial Black', 50)
    texto = font.render(':', True, (255, 255, 255))
    pos_texto = texto.get_rect()
    pos_texto.center = (120, 67)

    pos_relogio = (10, 10)

    # Pontos
    pontos = 0
    tamanho = pygame.font.SysFont('Arial Black', 30)
    text = tamanho.render('Pontuação: ' + str(pontos), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (460, 20)

    # Jogo
    display = pygame.display.set_mode([largura, altura])
    pygame.display.set_caption('Collectors')

    # Music
    pygame.mixer.music.load('data/MusicSons/sons/musica de fundo/Find Your Way Beat - Nana Kwabena.mp3')
    pygame.mixer.music.play(-1)

    # Sounds
    # shoot = pygame.mixer.Sound('MusicSons/8bit_gunloop_explosion.wav')
    colid = pygame.mixer.Sound('data/MusicSons/game-over2.wav')
    coletou = pygame.mixer.Sound('data/MusicSons/appear-online.ogg')

    # Teclas
    sair = True
    clock = pygame.time.Clock()
    timer = 20

    if __name__ == "__main__":
        while sair:
            clock.tick(20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False

                    # elif event.type == pygame.KEYDOWN:
                    #    if event.key == pygame.K_SPACE:
                    #        shoot.play()

            if (timer_relogio < 25):
                timer_relogio += 1

            else:
                tempo_segundo += 1
                texto = font.render(':' + str(tempo_segundo), True, (255, 255, 255))
                timer_relogio = 0

            # Update
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
                gameOver(pontos, tempo_segundo, 940, 600)
                colid.play()

            timer += 1
            if timer > 30:
                if random.random() < 0.2:
                    newLixo = Lixo(objectGroup, lixoGroup)
                    print('New Lixo!')

            colect = pygame.sprite.spritecollide(guy, lixoGroup, True, pygame.sprite.collide_mask)

            if colect:
                print('Coletou')
                pontos = pontos + 2
                text = tamanho.render('Pontuação: ' + str(pontos), True, (255, 255, 255))
                coletou.play()

            if timer > 30:
                if random.random() < 0.2:
                    newLixo2 = Lixo2(objectGroup, lixoGroup2)
                    print('New Lixo!')

            colect2 = pygame.sprite.spritecollide(guy, lixoGroup2, True, pygame.sprite.collide_mask)

            if colect2:
                print('Coletou')
                pontos = pontos + 1
                text = tamanho.render('Pontuação: ' + str(pontos), True, (255, 255, 255))
                coletou.play()

            # if sair == False:
            # Draw

            relogioimg = pygame.image.load('data/Imagens/relogio3.png')
            display.blit(fundojogo, (0, 0))  # Background
            display.blit(texto, pos_texto)
            display.blit(relogioimg, pos_relogio)
            display.blit(text, textRect)
            objectGroup.draw(display)
            pygame.display.update()

def credito():
    pygame.display.set_mode((940, 600))
    pygame.display.set_caption('Collectores')
    screen.fill((0,0,0))


def gameOver(pontos, time, largura, altura):
    global timer
    pygame.display.set_mode((940, 600))  # Define o tamanho da janela
    pygame.display.set_caption('Collectors')
    gameover2 = True
    while gameover2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.fill((0, 0, 0)) # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(gameover, (0, 0))  # plano de fundo da tela game over

        if 10 > pontos >= 0:
            screen.blit(umaEstrela, (80, 30))

            tamanho = pygame.font.SysFont('Arial Black', 30)
            text = tamanho.render(str(pontos) + ' Ponto(s) ', True, (196, 121, 8))
            textRect = text.get_rect()
            textRect.center = (290, 253)
            screen.blit(text, textRect)

            font = pygame.font.SysFont('Arial Black', 50)
            texto = font.render('s', True, (255, 255, 255))
            pos_texto = texto.get_rect()
            pos_texto.center = (80,30)
            screen.blit(texto, pos_texto)


            screen.blit(jogarp, (605, 80))
            screen.blit(sairp, (605, 420))
            screen.blit(creditop, (605, 250))

        elif 20 >= pontos >= 10 :
            screen.blit(duasEstrelas, (80, 35))

            tamanho = pygame.font.SysFont('Arial Black', 30)
            text = tamanho.render(str(pontos) + ' Ponto(s) ', True, (196, 121, 8))
            textRect = text.get_rect()
            textRect.center = (290, 253)
            screen.blit(text, textRect)

            font = pygame.font.SysFont('Arial Black', 50)
            texto = font.render('s', True, (255, 255, 255))
            pos_texto = texto.get_rect()
            pos_texto.center = (80,30)
            screen.blit(texto, pos_texto)

            screen.blit(jogarp, (605, 80))
            screen.blit(sairp, (605, 420))
            screen.blit(creditop, (605, 250))

        elif pontos >= 21:
            screen.blit(tresEstrelas, (80, 35))

            tamanho = pygame.font.SysFont('Arial Black', 30)
            text = tamanho.render(str(pontos) + ' Ponto(s) ', True, (196, 121, 8))
            textRect = text.get_rect()
            textRect.center = (290, 253)
            screen.blit(text, textRect)

            font = pygame.font.SysFont('Arial Black', 50)
            texto = font.render('s', True, (255, 255, 255))
            pos_texto = texto.get_rect()
            pos_texto.center = (80,30)
            screen.blit(texto, pos_texto)

            screen.blit(jogarp, (605, 80))
            screen.blit(sairp, (605, 420))
            screen.blit(creditop, (605, 250))

        pygame.display.update()

        while pygame.event.wait() or pygame.event.get():

            mouse = pygame.mouse.get_pos()
            if 605 + 308 > mouse[0] > 605 and 80 + 112 > mouse[1] > 80:
                screen.blit(jogarb, (605, 80))
                if pygame.mouse.get_pressed()[0]:
                    Jogo()

            else:
                screen.blit(jogarp, (605, 80))

            if 605 + 215 > mouse[0] > 605 and 420 + 83 > mouse[1] > 420:
                screen.blit(sairb, (605, 420))
                if pygame.mouse.get_pressed()[0]:
                    quit()

            else:
                screen.blit(sairp, (605, 420))

            if 605 + 215 > mouse[0] > 605 and 250 + 83 > mouse[1] > 250:
                screen.blit(creditob, (605, 250))
                #if pygame.mouse.get_pressed()[0]:
                #    credito()

            else:
                screen.blit(creditop, (605, 250))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.flip()


def menu():
    screen.blit(fundo, (0, 0))
    #screen.blit(titulo, (WIDTH / 4, 50))
    screen.blit(jogarp, (60, 200))
    #screen.blit(jogarb,(WIDTH /3,600))
    screen.blit(sairp, (600, 650))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 60 + 308 > mouse[0] > 60 and 200 + 112 > mouse[1] > 200:
            screen.blit(jogarb, (60, 200))
            if pygame.mouse.get_pressed()[0]:
                Jogo()


        else:
            screen.blit(jogarp, (60, 200))

        if 60 + 215 > mouse[0] > 60 and 325 + 83 > mouse[1] > 325:
            screen.blit(creditob, (60, 325))
            if pygame.mouse.get_pressed()[0]:
                credito()
        else:
            screen.blit(creditop, (60, 325))


        if 60 + 215 > mouse[0] > 60 and 450 + 83 > mouse[1] > 450:
            screen.blit(sairb, (60, 450))
            if pygame.mouse.get_pressed()[0]:
                quit()

        else:
            screen.blit(sairp, (60, 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()


menu()
quit()