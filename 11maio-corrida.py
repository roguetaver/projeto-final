# -*- coding: utf-8 -*-
"""
Created on Fri May 11 08:11:16 2018

@author: andre
"""


from classecavalinho1 import Cavalinho
import pygame
from pygame.locals import *
from random import randrange
from classebotao import botao
from classemensagem import mensagem
from funcaomov import movimento
from funcaolargada import largada
import time
# ===============   INICIALIZAÇÃO   ===============
pygame.init()
tela = pygame.display.set_mode((1200, 680), 0, 32)
pygame.display.set_caption('TURFE')
 
# carrega imagem de fundo 
fundo = pygame.image.load("pista.png")
fundo = pygame.transform.scale(fundo,(1200,660))


# cria cavalos
cavalinho1 = Cavalinho("cavalinho1.png",10,-20, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(600,800)/100)
cavalinho1_group = pygame.sprite.Group()
cavalinho1_group.add(cavalinho1)

cavalinho2 = Cavalinho("cavalinho2.png",10,90, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(600,800)/100)
cavalinho2_group = pygame.sprite.Group()
cavalinho2_group.add(cavalinho2)

cavalinho3 = Cavalinho("cavalinho3.png",10,200, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(600,800)/100)
cavalinho3_group = pygame.sprite.Group()
cavalinho3_group.add(cavalinho3)

cavalinho4 = Cavalinho("cavalinho4.png",10,310, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(600,800)/100)
cavalinho4_group = pygame.sprite.Group()
cavalinho4_group.add(cavalinho4)

cavalinho5 = Cavalinho("cavalinho5.png",10,420, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(600,800)/100)
cavalinho5_group = pygame.sprite.Group()
cavalinho5_group.add(cavalinho5)

cavalinho6 = Cavalinho("cavalinho6.png",10,530, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(600,800)/100)
cavalinho6_group = pygame.sprite.Group()
cavalinho6_group.add(cavalinho6)


#dicionario cavalo:escolha
cav_escolha = {}
cav_escolha[cavalinho1]="q"
cav_escolha[cavalinho2]="w"
cav_escolha[cavalinho3]="e"
cav_escolha[cavalinho4]="r"
cav_escolha[cavalinho5]="t"
cav_escolha[cavalinho6]="y"


#criar botões de escolha
Q = botao("Q.png",130,0)
Q_group = pygame.sprite.Group()
Q_group.add(Q)

W = botao("W.png",130,120)
W_group = pygame.sprite.Group()
W_group.add(W)

E = botao("E.png",130,230)
E_group = pygame.sprite.Group()
E_group.add(E)

R = botao("R.png",130,340)
R_group = pygame.sprite.Group()
R_group.add(R)

T = botao("T.png",130,450)
T_group = pygame.sprite.Group()
T_group.add(T)

Y = botao("Y.png",130,560)
Y_group = pygame.sprite.Group()
Y_group.add(Y)


#criar mensagens
derrota = mensagem("derrota.png",300,100)
derrota_group = pygame.sprite.Group()
derrota_group.add(derrota)

parabens = mensagem("vitoria.jpeg",300,100)
parabens_group = pygame.sprite.Group()
parabens_group.add(parabens)


#gerar tela do jogo inicial
tela.blit(fundo, (0, 0))
cavalinho1_group.draw(tela)
cavalinho2_group.draw(tela)
cavalinho3_group.draw(tela)
cavalinho4_group.draw(tela)
cavalinho5_group.draw(tela)
cavalinho6_group.draw(tela)
Q_group.draw(tela)
W_group.draw(tela)
E_group.draw(tela)
R_group.draw(tela)
T_group.draw(tela)
Y_group.draw(tela)
pygame.display.update()      #coloca a tela na janela


font = pygame.font.SysFont('Consolas', 80)
clock = pygame.time.Clock()
init = True 

    
# ===============   LOOPING PRINCIPAL   ===============

#escolha do jogador
escolha="errado"

while escolha=="errado":
    for event in pygame.event.get():
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_q:
                escolha="q"
            elif event.key==pygame.K_w:
                escolha="w"
            elif event.key==pygame.K_e:
                escolha="e"
            elif event.key==pygame.K_r:
                escolha="r"
            elif event.key==pygame.K_t:
                escolha="t"
            elif event.key==pygame.K_y:
                escolha="y"
     
        

    
    



rodando=True
acaba= True
ganhou = False
perdeu = False
cont = 0
#loop
while rodando:
    
    if init:
        if cont == 0:
            text1 = '5'
            tela.blit(font.render(text1, True, (0, 0, 0)), (500,300))
            pygame.display.update()
        elif cont == 30:
            text2 = '4'
            tela.blit(font.render(text2, True, (0, 0, 0)), (500,300))
            pygame.display.update()
        elif cont == 60:
            text3 = '3'
            tela.blit(font.render(text3, True, (0, 0, 0)), (500,300))
            pygame.display.update()
        elif cont == 90:
            text4 = '2'
            tela.blit(font.render(text4, True, (0, 0, 0)), (500,300))
            pygame.display.update()
        elif cont == 120:
            text5 = '1'
            tela.blit(font.render(text5, True, (0, 0, 0)), (500,300))
            pygame.display.update()
        elif cont == 150:
            text6 = 'GO!!!'
            tela.blit(font.render(text6, True, (0, 0, 0)), (500,300))
            pygame.display.update()
            init = False
        cont += 1
        
  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:      
            rodando = False
            
  #cavalinhos correm
    if not init:
        movimento (cavalinho1,cavalinho2,cavalinho3,cavalinho4,cavalinho5,cavalinho6)
        
        
  #gera saídas
    tela.blit(fundo, (0, 0))
    cavalinho1_group.draw(tela)
    cavalinho2_group.draw(tela)
    cavalinho3_group.draw(tela)
    cavalinho4_group.draw(tela)
    cavalinho5_group.draw(tela)
    cavalinho6_group.draw(tela)
    
   #testa se o cavalinho da escolha ganhou, e gera uma mensagem com a resposta na tela
    if cav_escolha[cavalinho1]==escolha and cavalinho1.rect.x>=1082:
        if cavalinho2.rect.x<1082 and cavalinho3.rect.x<1082 and cavalinho4.rect.x<1082 and cavalinho5.rect.x<1082 and cavalinho6.rect.x<1082:
            ganhou = True
            acaba=False
    elif cav_escolha[cavalinho2]==escolha and cavalinho2.rect.x>=1082:
        if cavalinho1.rect.x<1082 and cavalinho3.rect.x<1082 and cavalinho4.rect.x<1082 and cavalinho5.rect.x<1082 and cavalinho6.rect.x<1082:
            ganhou = True
            acaba=False
    elif cav_escolha[cavalinho3]==escolha and cavalinho3.rect.x>=1082:
        if cavalinho2.rect.x<1082 and cavalinho1.rect.x<1082 and cavalinho4.rect.x<1082 and cavalinho5.rect.x<1082 and cavalinho6.rect.x<1082:
            ganhou = True
            acaba=False
    elif cav_escolha[cavalinho4]==escolha and cavalinho4.rect.x>=1082:
        if cavalinho2.rect.x<1082 and cavalinho3.rect.x<1082 and cavalinho1.rect.x<1082 and cavalinho5.rect.x<1082 and cavalinho6.rect.x<1082:
            ganhou = True
            acaba=False
    elif cav_escolha[cavalinho5]==escolha and cavalinho5.rect.x>=1082:
        if cavalinho2.rect.x<1082 and cavalinho3.rect.x<1082 and cavalinho4.rect.x<1082 and cavalinho1.rect.x<1082 and cavalinho6.rect.x<1082:
            ganhou = True
            acaba=False
    elif cav_escolha[cavalinho6]==escolha and cavalinho6.rect.x>=1082:
        if cavalinho2.rect.x<1082 and cavalinho3.rect.x<1082 and cavalinho4.rect.x<1082 and cavalinho5.rect.x<1082 and cavalinho1.rect.x<1082:
            ganhou = True
            acaba=False
    elif cavalinho1.rect.x >= 1083 or cavalinho2.rect.x >= 1083 or cavalinho3.rect.x >= 1083 or cavalinho4.rect.x >= 1083 or cavalinho5.rect.x >= 1083 or cavalinho6.rect.x >= 1083:
        if acaba:
            perdeu = True
    if perdeu:
        derrota_group.draw(tela)
    if ganhou:
        parabens_group.draw(tela)
    if not init:
        pygame.display.update()      #coloca a tela na janela
    
pygame.display.quit()