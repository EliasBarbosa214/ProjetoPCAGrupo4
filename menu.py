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
sairp = pygame.image.load("data/Imagens/fecha2.png")
sairb = pygame.image.load("data/Imagens/SAIR.png")
fundo = pygame.image.load("data/Imagens/fundomenu.png")
gameover = pygame.image.load('data/Imagens/GameOver1.png')
pontos = 0



umaEstrela = pygame.image.load('data/Imagens/1estrelas.png')
duasEstrelas = pygame.image.load('data/Imagens/2estrelas.png')
tresEstrelas = pygame.image.load('data/Imagens/3estrelas.png')


pygame.mixer.music.load('data/MusicSons/sons/musica de fundo/menu.mp3')
pygame.mixer.music.play(-1)

'''def gameOver(pontos, time, largura, altura):
    pygame.display.set_mode((largura, altura))  # Define o tamanho da janela
    pygame.display.set_caption('Collectors')
    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0,
                     0))  # apaga a tela para impressão de movimento, preenchendo toda tela de preto (Tem q vir primeiro)
        screen.blit(gameover, (0, 0))  # plano de fundo da tela game over
        screen.blit(pontos, (100, 100))  # a posição foi chutada
        screen.blit(time, (200, 100))  # a posição foi chutada
        if pontos < 10:
            screen.blit(umaEstrela, (100, 100))
        elif 10 > pontos < 50:
            screen.blit(duasEstrelas, (100, 100))
        elif 50 > pontos < 100:
            screen.blit(tresEstrelas, (100, 100))
        pygame.display.update()'''

def menu():
    screen.blit(fundo, (0, 0))
    #screen.blit(titulo, (WIDTH / 4, 50))
    screen.blit(jogarp, (120, 650))
    #screen.blit(jogarb,(WIDTH /3,600))
    screen.blit(sairp, (600, 650))
    # screen.blit(sairb,(WIDTH /3,600))
    pygame.display.flip()

    while pygame.event.wait() or pygame.event.get():

        mouse = pygame.mouse.get_pos()
        if 120 + 308 > mouse[0] > 120 and 490 + 112 > mouse[1] > 490:
            screen.blit(jogarb, (120, 490))
            if pygame.mouse.get_pressed()[0]:
                largura = 940
                altura = 600
                fundojogo = pygame.image.load('data/Imagens/cidade2.jpg')
                #fundojogo = pygame.transform.scale(fundojogo, [940, 600])


                # Object Grupo
                objectGroup = pygame.sprite.Group()
                redguyGroup = pygame.sprite.Group()
                lixoGroup = pygame.sprite.Group()
                shootGroup = pygame.sprite.Group()
                lixoGroup2 = pygame.sprite.Group()

                guy = Guy(objectGroup)

                # Timer
                timer_relogio = 0
                tempo_segundo = 0

                font = pygame.font.SysFont('Arial Black', 50)
                texto = font.render(':', True, (255, 255, 255))
                pos_texto = texto.get_rect()
                pos_texto.center = (120, 67)

                pos_relogio = (10,10)

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

                        def GameOver():
                            display.blit(gameover, (0,0))

                        collision = pygame.sprite.spritecollide(guy, redguyGroup, False, pygame.sprite.collide_mask)

                        #umaEstrela = pygame.image.load(gameover)

                        umaEstrela = pygame.image.load('data/Imagens/GameOver1.png')

                        if collision:
                            print('Game OVER!')
                            tamanho = pygame.font.SysFont('Arial Black', 60)
                            text = tamanho.render('Pontuação: ' + str(pontos), True, (255, 255, 255))
                            textRect.center = (200, 40)
    
                            font = pygame.font.SysFont('Arial Black', 70)
                            #texto = font.render(':', True, (255, 255, 255))
                            #pos_texto = texto.get_rect()
                            pos_texto.center = (710, 60)
                            pos_relogio = (600, 10)


                            sair = False
                            '''gameOver(pontos, timer, 940, 600)'''
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

                        if sair == False:
                            print('Você terminou com total de: {} pontos.'.format(pontos))
                            print('Você terminou com total de: {} segundos.'.format(tempo_segundo))

                        # Draw

                        relogioimg = pygame.image.load('data/Imagens/relogio3.png')
                        display.blit(fundojogo, (0, 0))  # Background
                        display.blit(texto, pos_texto)
                        display.blit(relogioimg, pos_relogio)
                        display.blit(text, textRect)
                        objectGroup.draw(display)
                        pygame.display.update()


        else:
            screen.blit(jogarp, (120, 490))


        if 600 + 215 > mouse[0] > 600 and 500 + 83 > mouse[1] > 500:
            screen.blit(sairb, (600, 500))
            if pygame.mouse.get_pressed()[0]:
                quit()

        else:
            screen.blit(sairp, (600, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()


menu()
quit()