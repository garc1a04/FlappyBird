import pygame
import random

"""
Author: Guilherme Garcia Monteiro
"""

#Criando a tela
largura = 500
altura = 650
tela = pygame.display.set_mode((largura,altura))
frames = pygame.time.Clock()

#imagens
passaro = pygame.image.load("Imagens\\birdComanemia.png")
fundo = pygame.image.load("Imagens\\bg.png")
chao = pygame.image.load("Imagens\\ground.png")
restart = pygame.image.load("Imagens\\restart.png")

#Variaveis
chaoX = 20
canoX = 800
canoY = (altura//2)+20
andarX = 20
andarY = altura//2
velocidade = 0
clicou = False
run = True
voando = False
passaroAux = passaro

def canos(X,Y,aleatorio):
    cano = pygame.image.load("Imagens\\pipe.png")
    tela.blit(cano,(X,Y+aleatorio)) 
       
    cano = pygame.transform.flip(cano, False, True)
    tela.blit(cano,(X,-Y+aleatorio))


aleatorio = random.randint(0, 10)
#Repeticao infinita para o jogo
while True:    
    frames.tick(60)
    tela.blit(fundo, (0, 0))
    tela.blit(passaro, (andarX, andarY))
    canos(canoX,canoY,aleatorio)
    tela.blit(chao, (chaoX, 600))
    
    if(andarY >= 565):
        run = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if(run):
            if pygame.mouse.get_pressed()[0] == 1 and clicou == False:
                clicou = True
                voando = True
                andarY-=10
                velocidade = -10
            if pygame.mouse.get_pressed()[0] == 0:
                clicou = False
            
    if(run):
        chaoX-=4
        if abs(chaoX) > 35:
            chaoX = 0
            
        if(voando):
            #Gravidade
            velocidade += 0.5
            if(andarY < 565):
                andarY += velocidade
                
            #Colisão
            #TODO Fazer a colisão de baixo...
            colisaoX = canoY+aleatorio
            if(andarX >= canoX-50 and canoX >= -20):
                if(andarY+35 >= canoY+aleatorio):
                    run = False
                    
            #Cano andando
            canoX-=4
            if(canoX < -100):
                canoX = 600
                aleatorio = random.randint(-200, 200)
            passaro = pygame.transform.rotate(passaroAux, velocidade*-2)
    pygame.display.update()