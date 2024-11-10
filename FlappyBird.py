import pygame
import random

"""
Author: Guilherme Garcia Monteiro
"""
pygame.init()

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
cano = pygame.image.load("Imagens\\pipe.png")

#Variaveis
chaoX = 20
espaco = 20
canoX = 800
canoY = (altura//2)+espaco
andarX = 20
andarY = altura//2
pontucao = 0
velocidade = 0
clicou = False
run = True
pontuou = True
passaroAux = passaro

def canos(X,Y,aleatorio):
    cano = pygame.image.load("Imagens\\pipe.png")
    tela.blit(cano,(X,Y+aleatorio)) 
    cano = pygame.transform.flip(cano, False, True)
    tela.blit(cano,(X,-Y+aleatorio))

def desenhos():
    tela.blit(fundo, (0, 0))
    tela.blit(passaro, (andarX, andarY))
    canos(canoX,canoY,aleatorio)
    tela.blit(chao, (chaoX, 600))


white = (255,255,255)
fonte = pygame.font.SysFont('Bauhaus 93', 60)
aleatorio = random.randint(0, 10)
#Repeticao infinita para o jogo
while True:
    frames.tick(60)
    
    #caixas de colisões
    canoRectBaixo = pygame.draw.rect(tela,(0,0,0),(canoX, canoY+aleatorio,74,560))
    canoRectCima = pygame.draw.rect(tela,(0,0,0),(canoX, -canoY+aleatorio,74,560))
    passaroRect = pygame.draw.rect(tela,(0,0,0),(andarX+5, andarY+5,45,35))
    
    #tela
    desenhos()
    
    #pontuacao
    img = fonte.render(str(pontucao), True, white)
    tela.blit(img, (largura/2,0))
    
    #O personagem encostou no chao
    if(andarY >= 565):
        run = False
    
    #Pegar eventos...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if pygame.mouse.get_pressed()[0] == 1 and clicou == False and run:
            clicou = True
            andarY-=10
            velocidade = -10
        if pygame.mouse.get_pressed()[0] == 0 and run:
            clicou = False
            
    if(run):
        chaoX-=4
        if abs(chaoX) > 35:
            chaoX = 0
            
        #Gravidade
        velocidade += 0.5
        if(andarY < 565):
            andarY += velocidade
            
        #Colisao
        if(passaroRect.colliderect(canoRectBaixo) or passaroRect.colliderect(canoRectCima)):
            run = False
        
        
        #Pontuação
        if(passaroRect.left > canoRectCima.right and pontuou):
            pontucao+=1
            pontuou = False
        
        #Cano andando
        canoX-=4
        if(canoX < -100):
            pontuou = True
            canoX = 600
            aleatorio = random.randint(-150, 150)

        
        passaro = pygame.transform.rotate(passaroAux, velocidade*-2)
    #Reiniciar
    else:
        restartRect = pygame.draw.rect(tela,(0,0,0),(largura//2 - 50, altura//2-20,120,42))
        tela.blit(restart, (largura//2 - 50,altura//2 - 20))
        pos = pygame.mouse.get_pos()
        
        if(restartRect.collidepoint(pos)):
            if(pygame.mouse.get_pressed()[0] == 1):
                chaoX = 20
                canoX = 800
                andarY = altura//2
                pontucao = 0
                velocidade = 0
                run = True
        
    pygame.display.update()