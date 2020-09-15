import pygame
from random import randint
pygame.init()

janela = pygame.display.set_mode((1200,650))
pygame.display.set_caption("Collectors")

x = 501   #Meio 501 max esquerda: 150 max direita: 870
y = 420
pos_x = 411
pos_y = -20
pos_y_a = -20
pos_y_b = -20
pos_y_d = -20
pos_y_f = -20
timer = 0
tempo_segundo = 0

velocidade = 25
velocidade_outros = 10

fundo = pygame.image.load('cidade.jpg')
perso = pygame.image.load('personagem3.png')
lixo2 = pygame.image.load('lixo1.png')
garrafa = pygame.image.load('garrafa1.png')
garrafa2 = pygame.image.load('garrafa1.png')
caixa = pygame.image.load('jornal.png')
refri = pygame.image.load('refri.png')
relogio = pygame.image.load('relogio2.png')

font = pygame.font.SysFont('Arial Black', 50)
texto = font.render(':', True, (109, 212, 205))
pos_texto = texto.get_rect()
pos_texto.center = (125, 67)

janela_aberta = True
while janela_aberta:
    pygame.time.delay(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and x <= 870:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 150:
        x -= velocidade

    if (pos_y_a >= 1200) and (pos_y_b >= 1200) and (pos_y_d >= 1200) and (pos_y_f >= 1200):
        pos_y_a = randint(-1500, 0) #saco de lixo
        pos_y_b = randint(-1500, 0) #garrafa
        pos_y_d = randint(-1500, 0) #pizza
        pos_y_f = randint(-1500, 0) #refri

    if (timer < 25):
        timer += 1

    else:
        tempo_segundo += 1
        texto = font.render(':' +str(tempo_segundo),  True, (109, 212, 205))
        timer = 0

    pos_y_a += velocidade_outros -3
    pos_y_b += velocidade_outros -1.5
    pos_y_d += velocidade_outros -1.2
    pos_y_f += velocidade_outros -2

    janela.blit(fundo, (0,0))
    janela.blit(perso, (x,y))
    janela.blit(refri, (pos_x + 350, pos_y_f -350))
    janela.blit(lixo2, (pos_x - 100, pos_y_a -600))
    janela.blit(garrafa, (pos_x + 50, pos_y_b -640))
    janela.blit(caixa, (pos_x + 200, pos_y_d  -250))
    janela.blit(relogio, (15, 10))
    janela.blit(texto, pos_texto)

    pygame.display.update()

pygame.quit()