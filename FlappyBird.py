import pygame

"""
Author: Guilherme Garcia Monteiro

"""



#Criando a tela
largura = 300
altura = 400
tela = pygame.display.set_mode((largura,altura))

#Repeticao infinita para o jogo
while True:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            exit()


    pygame.display.update()
    