import pygame

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

#Variaveis
chaoX = 0
andarX = 0
andarY = altura//2
velocidade = 0
clicou = False
run = True

#Repeticao infinita para o jogo
while run:
    frames.tick(60)
    
    tela.fill((0,0,0))
    tela.blit(fundo, (0, 0))
    tela.blit(passaro, (andarX, andarY))
    tela.blit(chao, (chaoX, 600))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if pygame.mouse.get_pressed()[0] == 1 and clicou == False:
            clicou = True
            andarY-=10
            velocidade = -10
        if pygame.mouse.get_pressed()[0] == 0:
            clicou = False
    
    #Chão andando
    chaoX-=4
    if abs(chaoX) > 35:
        chaoX = 0
    
    #Gravidade
    velocidade += 0.5
    if(andarY < 565):
        andarY += velocidade
    pygame.display.update()