# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:22:04 2018

@author: mihan
"""

from classecavalinho1 import Cavalinho
import pygame
from pygame.locals import *
from random import randrange
from classebotao import botao
from classetexto import texto
from funcaomov import movimento
from classemensagem import mensagem
from classejogador import jogador

# ===============   INICIALIZAÇÃO   ===================
pygame.init()
largura, altura = 1100, 650
hw = largura/2
hh = altura/2
area = largura * altura
tela = pygame.display.set_mode((largura, altura))
FPS = 30
pygame.display.set_caption('TURFE')


 
# carrega imagem de fundo 
fundo = pygame.image.load("pistamov.png")
fundo = pygame.transform.scale(fundo,(5000,altura))

v = 0
font = pygame.font.SysFont('Consolas', 80)
font1 = pygame.font.SysFont('Consolas', 25)
font2 = pygame.font.SysFont('Consolas', 35)
clock = pygame.time.Clock()
largada = True 
init1 = True
linha = 800

rodando=True
escolha=True
acaba= True
ganhou = False
perdeu = False
cont = 0
escolha=True
vez=1
comeco=True
ok=True

    # cria cavalos
cavalinho1 = Cavalinho("cavalinho1.png",10,60, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
cavalinho1_group = pygame.sprite.Group()
cavalinho1_group.add(cavalinho1)

cavalinho2 = Cavalinho("cavalinho2.png",10,155, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
cavalinho2_group = pygame.sprite.Group()
cavalinho2_group.add(cavalinho2)

cavalinho3 = Cavalinho("cavalinho3.png",10,245, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
cavalinho3_group = pygame.sprite.Group()
cavalinho3_group.add(cavalinho3)

cavalinho4 = Cavalinho("cavalinho4.png",10,340, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
cavalinho4_group = pygame.sprite.Group()
cavalinho4_group.add(cavalinho4)

cavalinho5 = Cavalinho("cavalinho5.png",10,430, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
cavalinho5_group = pygame.sprite.Group()
cavalinho5_group.add(cavalinho5)

cavalinho6 = Cavalinho("cavalinho6.png",10,535,
            randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
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
Q = botao("Q.png",130,80)
Q_group = pygame.sprite.Group()
Q_group.add(Q)

W = botao("W.png",130,180)
W_group = pygame.sprite.Group()
W_group.add(W)

E = botao("E.png",130,270)
E_group = pygame.sprite.Group()
E_group.add(E)

R = botao("R.png",130,365)
R_group = pygame.sprite.Group()
R_group.add(R)

T = botao("T.png",130,455)
T_group = pygame.sprite.Group()
T_group.add(T)

Y = botao("Y.png",130,550)
Y_group = pygame.sprite.Group()
Y_group.add(Y)


#criar mensagens
cavalinho11 = mensagem("cavalinho1.png",30,60, 60,60)
cavalinho11_group = pygame.sprite.Group()
cavalinho11_group.add(cavalinho11)

cavalinho12 = mensagem("cavalinho2.png",30,60,60,60)
cavalinho12_group = pygame.sprite.Group()
cavalinho12_group.add(cavalinho12)

cavalinho13 = mensagem("cavalinho3.png",30,60, 60,60)
cavalinho13_group = pygame.sprite.Group()
cavalinho13_group.add(cavalinho13)

cavalinho14 = mensagem("cavalinho4.png",30,60, 60,60)
cavalinho14_group = pygame.sprite.Group()
cavalinho14_group.add(cavalinho14)

cavalinho15 = mensagem("cavalinho5.png",30,60, 60,60)
cavalinho15_group = pygame.sprite.Group()
cavalinho15_group.add(cavalinho15)

cavalinho16 = mensagem("cavalinho6.png",30,60, 60,60)
cavalinho16_group = pygame.sprite.Group()
cavalinho16_group.add(cavalinho16)

cavalinho21 = mensagem("cavalinho1.png",100,60, 60,60)
cavalinho21_group = pygame.sprite.Group()
cavalinho21_group.add(cavalinho21)

cavalinho22 = mensagem("cavalinho2.png",100,60,60,60)
cavalinho22_group = pygame.sprite.Group()
cavalinho22_group.add(cavalinho22)

cavalinho23 = mensagem("cavalinho3.png",100,60, 60,60)
cavalinho23_group = pygame.sprite.Group()
cavalinho23_group.add(cavalinho23)

cavalinho24 = mensagem("cavalinho4.png",100,60, 60,60)
cavalinho24_group = pygame.sprite.Group()
cavalinho24_group.add(cavalinho24)

cavalinho25 = mensagem("cavalinho5.png",100,60, 60,60)
cavalinho25_group = pygame.sprite.Group()
cavalinho25_group.add(cavalinho25)

cavalinho26 = mensagem("cavalinho6.png",100,60, 60,60)
cavalinho26_group = pygame.sprite.Group()
cavalinho26_group.add(cavalinho26)

cavalinho31 = mensagem("cavalinho1.png",100,60, 60,60)
cavalinho31_group = pygame.sprite.Group()
cavalinho31_group.add(cavalinho31)

cavalinho32 = mensagem("cavalinho2.png",100,60,60,60)
cavalinho32_group = pygame.sprite.Group()
cavalinho32_group.add(cavalinho32)

cavalinho33 = mensagem("cavalinho3.png",100,60, 60,60)
cavalinho33_group = pygame.sprite.Group()
cavalinho33_group.add(cavalinho33)

cavalinho34 = mensagem("cavalinho4.png",100,60, 60,60)
cavalinho34_group = pygame.sprite.Group()
cavalinho34_group.add(cavalinho34)

cavalinho35 = mensagem("cavalinho5.png",100,60, 60,60)
cavalinho35_group = pygame.sprite.Group()
cavalinho35_group.add(cavalinho35)

cavalinho36 = mensagem("cavalinho6.png",100,60, 60,60)
cavalinho36_group = pygame.sprite.Group()
cavalinho36_group.add(cavalinho36)

cavalinho41 = mensagem("cavalinho1.png",100,60, 60,60)
cavalinho41_group = pygame.sprite.Group()
cavalinho41_group.add(cavalinho41)

cavalinho42 = mensagem("cavalinho2.png",100,60,60,60)
cavalinho42_group = pygame.sprite.Group()
cavalinho42_group.add(cavalinho42)

cavalinho43 = mensagem("cavalinho3.png",100,60, 60,60)
cavalinho43_group = pygame.sprite.Group()
cavalinho43_group.add(cavalinho43)

cavalinho44 = mensagem("cavalinho4.png",100,60, 60,60)
cavalinho44_group = pygame.sprite.Group()
cavalinho44_group.add(cavalinho44)

cavalinho45 = mensagem("cavalinho5.png",100,60, 60,60)
cavalinho45_group = pygame.sprite.Group()
cavalinho45_group.add(cavalinho45)

cavalinho46 = mensagem("cavalinho6.png",100,60, 60,60)
cavalinho46_group = pygame.sprite.Group()
cavalinho46_group.add(cavalinho46)

cavalinho51 = mensagem("cavalinho1.png",100,60, 60,60)
cavalinho51_group = pygame.sprite.Group()
cavalinho51_group.add(cavalinho51)

cavalinho52 = mensagem("cavalinho2.png",100,60,60,60)
cavalinho52_group = pygame.sprite.Group()
cavalinho52_group.add(cavalinho52)

cavalinho53 = mensagem("cavalinho3.png",100,60, 60,60)
cavalinho53_group = pygame.sprite.Group()
cavalinho53_group.add(cavalinho53)

cavalinho54 = mensagem("cavalinho4.png",100,60, 60,60)
cavalinho54_group = pygame.sprite.Group()
cavalinho54_group.add(cavalinho54)

cavalinho55 = mensagem("cavalinho5.png",100,60, 60,60)
cavalinho55_group = pygame.sprite.Group()
cavalinho55_group.add(cavalinho55)

cavalinho56 = mensagem("cavalinho6.png",100,60, 60,60)
cavalinho56_group = pygame.sprite.Group()
cavalinho56_group.add(cavalinho56)

cavalinho61 = mensagem("cavalinho1.png",100,60, 60,60)
cavalinho61_group = pygame.sprite.Group()
cavalinho61_group.add(cavalinho61)

cavalinho62 = mensagem("cavalinho2.png",100,60,60,60)
cavalinho62_group = pygame.sprite.Group()
cavalinho62_group.add(cavalinho62)

cavalinho63 = mensagem("cavalinho3.png",100,60, 60,60)
cavalinho63_group = pygame.sprite.Group()
cavalinho63_group.add(cavalinho63)

cavalinho64 = mensagem("cavalinho4.png",100,60, 60,60)
cavalinho64_group = pygame.sprite.Group()
cavalinho64_group.add(cavalinho64)

cavalinho65 = mensagem("cavalinho5.png",100,60, 60,60)
cavalinho65_group = pygame.sprite.Group()
cavalinho65_group.add(cavalinho65)

cavalinho66 = mensagem("cavalinho6.png",100,60, 60,60)
cavalinho66_group = pygame.sprite.Group()
cavalinho66_group.add(cavalinho66)

p1 = mensagem("p1.png",10,10, 130, 87)
p1_group = pygame.sprite.Group()
p1_group.add(p1)

p2 = mensagem("p2.png",150,10, 130, 87)
p2_group = pygame.sprite.Group()
p2_group.add(p2)

p3 = mensagem("p3.png",290,10, 130, 87)
p3_group = pygame.sprite.Group()
p3_group.add(p3)

p4 = mensagem("p4.png",430,10, 130, 87)
p4_group = pygame.sprite.Group()
p4_group.add(p4)

p5 = mensagem("p5.png",570,10, 130, 87)
p5_group = pygame.sprite.Group()
p5_group.add(p5)

p6 = mensagem("p6.png",710,10, 130, 87)
p6_group = pygame.sprite.Group()
p6_group.add(p6)

#criar jogadores
J1 = jogador("jogador 1", 100)
J1_group = pygame.sprite.Group()
J1_group.add(J1)
   
J2 = jogador("jogador 2", 100)
J2_group = pygame.sprite.Group()
J2_group.add(J2)

J3 = jogador("jogador 3", 100)
J3_group = pygame.sprite.Group()
J3_group.add(J3)

J4 = jogador("jogador 4", 100)
J4_group = pygame.sprite.Group()
J4_group.add(J4)

J5 = jogador("jogador 5", 100)
J5_group = pygame.sprite.Group()
J5_group.add(J5)

J6 = jogador("jogador 6", 100)
J6_group = pygame.sprite.Group()
J6_group.add(J6)
# ===============   LOOPING PRINCIPAL   ===============

#loop
while rodando:
    clock.tick(30)
    
    while comeco:    
        
        #gerar tela do jogo inicial
        tela.blit(fundo, (0, 0))
        p1_group.draw(tela)
        p2_group.draw(tela)
        p3_group.draw(tela)
        p4_group.draw(tela)
        p5_group.draw(tela)
        p6_group.draw(tela)
        cavalinho1_group.draw(tela)
        cavalinho2_group.draw(tela)
        cavalinho3_group.draw(tela)
        cavalinho4_group.draw(tela)
        cavalinho5_group.draw(tela)
        cavalinho6_group.draw(tela)
        tela.blit(font1.render(str(J1.carteira), True, (0, 0, 0)), (40,40))
        tela.blit(font1.render(str(J2.carteira), True, (0, 0, 0)), (180,40))  
        tela.blit(font1.render(str(J3.carteira), True, (0, 0, 0)), (320,40))  
        tela.blit(font1.render(str(J4.carteira), True, (0, 0, 0)), (460,40))  
        tela.blit(font1.render(str(J5.carteira), True, (0, 0, 0)), (600,40))  
        tela.blit(font1.render(str(J6.carteira), True, (0, 0, 0)), (740,40))  
        pygame.display.update()
        Q_group.draw(tela)
        W_group.draw(tela)
        E_group.draw(tela)
        R_group.draw(tela)
        T_group.draw(tela)
        Y_group.draw(tela)
        pygame.display.update()  #coloca a tela na janela
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:      
                rodando = False


        #escolha do jogador 1
        while vez == 1:
             tela.blit(font2.render("Jogador {0}, escolha o seu cavalo".format(vez), True, (0, 0, 0)), (250,400))
             pygame.display.update()
             for event in pygame.event.get():
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_q:
                        aposta="q"
                        quantidade=10
                        while ok:
                            cavalinho11_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        vez=2
                    elif event.key==pygame.K_w:
                        aposta="w"
                        quantidade=10
                        while ok:
                            cavalinho12_group.draw(tela)                            
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        vez=2
                    elif event.key==pygame.K_e:
                        aposta="e"
                        quantidade=10
                        while ok:
                            cavalinho13_group.draw(tela)                           
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        vez=2
                    elif event.key==pygame.K_r:
                        aposta="r"
                        quantidade=10
                        while ok:
                            cavalinho14_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        vez=2
                    elif event.key==pygame.K_t:
                        aposta="t"
                        quantidade=10
                        while ok:
                            cavalinho15_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        vez=2
                    elif event.key==pygame.K_y:
                        aposta="y"
                        quantidade=10
                        while ok:
                            cavalinho16_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        vez=2
                    elif event.key==pygame.K_SPACE:
                        ok=False
                        vez=2
                        aposta="x"
                        quantidade=1
        
        #mudanças no jogador 1
        ok=True
        J1.aposta(aposta, quantidade)
        J1.ganha_grana(-quantidade)
        
        #escolha do jogador 2
        while vez == 2:
             tela.blit(font2.render("Jogador 2, escolha o seu cavalo".format(vez), True, (0, 0, 0)), (250,400))
             pygame.display.update()
             for event in pygame.event.get():
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_q:
                        aposta="q"
                        quantidade=10
                        while ok:
                            cavalinho31_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=3
                    elif event.key==pygame.K_w:
                        aposta="w"
                        quantidade=10
                        while ok:
                            cavalinho32_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_w:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=3
                    elif event.key==pygame.K_e:
                        aposta="e"
                        quantidade=10
                        while ok:
                            cavalinho33_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_e:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=3
                    elif event.key==pygame.K_r:
                        aposta="r"
                        quantidade=10
                        while ok:
                            cavalinho34_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_r:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=3
                    elif event.key==pygame.K_t:
                        aposta="t"
                        quantidade=10
                        while ok:
                            cavalinho35_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_t:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=3
                    elif event.key==pygame.K_y:
                        aposta="y"
                        quantidade=10
                        while ok:
                            cavalinho36_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_y:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=3
                    elif event.key==pygame.K_SPACE:
                        ok=False
                        vez=3
                        comeco=False
                        aposta="x"
                        quantidade=1
                        
        #mudanças no jogador 2
        J2.aposta(aposta, quantidade)
        J2.ganha_grana(-quantidade)
        
        tela.blit(font1.render(str(J1.carteira), True, (0, 0, 0)), (40,40))
        tela.blit(font1.render(str(J2.carteira), True, (0, 0, 0)), (180,40))  
        tela.blit(font1.render(str(J3.carteira), True, (0, 0, 0)), (320,40))  
        tela.blit(font1.render(str(J4.carteira), True, (0, 0, 0)), (460,40))  
        tela.blit(font1.render(str(J5.carteira), True, (0, 0, 0)), (600,40))  
        tela.blit(font1.render(str(J6.carteira), True, (0, 0, 0)), (740,40))  
        
        #escolha do jogador 3
        while vez == 3:
             tela.blit(font2.render("Jogador 3, escolha o seu cavalo".format(vez), True, (0, 0, 0)), (250,400))
             pygame.display.update()
             for event in pygame.event.get():
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_q:
                        aposta="q"
                        quantidade=10
                        while ok:
                            cavalinho31_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=4
                    elif event.key==pygame.K_w:
                        aposta="w"
                        quantidade=10
                        while ok:
                            cavalinho32_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_w:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=4
                    elif event.key==pygame.K_e:
                        aposta="e"
                        quantidade=10
                        while ok:
                            cavalinho33_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_e:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=4
                    elif event.key==pygame.K_r:
                        aposta="r"
                        quantidade=10
                        while ok:
                            cavalinho34_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_r:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=4
                    elif event.key==pygame.K_t:
                        aposta="t"
                        quantidade=10
                        while ok:
                            cavalinho35_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_t:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=4
                    elif event.key==pygame.K_y:
                        aposta="y"
                        quantidade=10
                        while ok:
                            cavalinho36_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_y:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=4
                    elif event.key==pygame.K_SPACE:
                        ok=False
                        vez=4
                        comeco=False
                        aposta="x"
                        quantidade=1
    
        #mudanças no jogador 3
        J3.aposta(aposta, quantidade)
        J3.ganha_grana(-quantidade)

        tela.blit(font1.render(str(J1.carteira), True, (0, 0, 0)), (40,40))
        tela.blit(font1.render(str(J2.carteira), True, (0, 0, 0)), (180,40))  
        tela.blit(font1.render(str(J3.carteira), True, (0, 0, 0)), (320,40))  
        tela.blit(font1.render(str(J4.carteira), True, (0, 0, 0)), (460,40))  
        tela.blit(font1.render(str(J5.carteira), True, (0, 0, 0)), (600,40))  
        tela.blit(font1.render(str(J6.carteira), True, (0, 0, 0)), (740,40))  
        
        #escolha do jogador 4
        while vez == 4:
             tela.blit(font2.render("Jogador 4, escolha o seu cavalo".format(vez), True, (0, 0, 0)), (250,400))
             pygame.display.update()
             for event in pygame.event.get():
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_q:
                        aposta="q"
                        quantidade=10
                        while ok:
                            cavalinho41_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=5
                    elif event.key==pygame.K_w:
                        aposta="w"
                        quantidade=10
                        while ok:
                            cavalinho42_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_w:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=5
                    elif event.key==pygame.K_e:
                        aposta="e"
                        quantidade=10
                        while ok:
                            cavalinho43_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_e:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=5
                    elif event.key==pygame.K_r:
                        aposta="r"
                        quantidade=10
                        while ok:
                            cavalinho44_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_r:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=5
                    elif event.key==pygame.K_t:
                        aposta="t"
                        quantidade=10
                        while ok:
                            cavalinho45_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_t:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=5
                    elif event.key==pygame.K_y:
                        aposta="y"
                        quantidade=10
                        while ok:
                            cavalinho46_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_y:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=5
                    elif event.key==pygame.K_SPACE:
                        ok=False
                        vez=5
                        comeco=False
                        aposta="x"
                        quantidade=1
    
        #mudanças no jogador 4
        J4.aposta(aposta, quantidade)
        J4.ganha_grana(-quantidade)

        tela.blit(font1.render(str(J1.carteira), True, (0, 0, 0)), (40,40))
        tela.blit(font1.render(str(J2.carteira), True, (0, 0, 0)), (180,40))  
        tela.blit(font1.render(str(J3.carteira), True, (0, 0, 0)), (320,40))  
        tela.blit(font1.render(str(J4.carteira), True, (0, 0, 0)), (460,40))  
        tela.blit(font1.render(str(J5.carteira), True, (0, 0, 0)), (600,40))  
        tela.blit(font1.render(str(J6.carteira), True, (0, 0, 0)), (740,40))  
                
        #escolha do jogador 3
        while vez == 5:
             tela.blit(font2.render("Jogador 5, escolha o seu cavalo".format(vez), True, (0, 0, 0)), (250,400))
             pygame.display.update()
             for event in pygame.event.get():
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_q:
                        aposta="q"
                        quantidade=10
                        while ok:
                            cavalinho51_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=6
                    elif event.key==pygame.K_w:
                        aposta="w"
                        quantidade=10
                        while ok:
                            cavalinho52_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_w:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=6
                    elif event.key==pygame.K_e:
                        aposta="e"
                        quantidade=10
                        while ok:
                            cavalinho53_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_e:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=6
                    elif event.key==pygame.K_r:
                        aposta="r"
                        quantidade=10
                        while ok:
                            cavalinho54_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_r:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=6
                    elif event.key==pygame.K_t:
                        aposta="t"
                        quantidade=10
                        while ok:
                            cavalinho55_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_t:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=6
                    elif event.key==pygame.K_y:
                        aposta="y"
                        quantidade=10
                        while ok:
                            cavalinho56_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_y:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=6
                    elif event.key==pygame.K_SPACE:
                        ok=False
                        vez=6
                        comeco=False
                        aposta="x"
                        quantidade=1
    
        #mudanças no jogador 4
        J5.aposta(aposta, quantidade)
        J5.ganha_grana(-quantidade)

        tela.blit(font1.render(str(J1.carteira), True, (0, 0, 0)), (40,40))
        tela.blit(font1.render(str(J2.carteira), True, (0, 0, 0)), (180,40))  
        tela.blit(font1.render(str(J3.carteira), True, (0, 0, 0)), (320,40))  
        tela.blit(font1.render(str(J4.carteira), True, (0, 0, 0)), (460,40))  
        tela.blit(font1.render(str(J5.carteira), True, (0, 0, 0)), (600,40))  
        tela.blit(font1.render(str(J6.carteira), True, (0, 0, 0)), (740,40))  

        #escolha do jogador 3
        while vez == 3:
             tela.blit(font2.render("Jogador 6, escolha o seu cavalo".format(vez), True, (0, 0, 0)), (250,400))
             pygame.display.update()
             for event in pygame.event.get():
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_q:
                        aposta="q"
                        quantidade=10
                        while ok:
                            cavalinho61_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=0
                    elif event.key==pygame.K_w:
                        aposta="w"
                        quantidade=10
                        while ok:
                            cavalinho62_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_w:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=0
                    elif event.key==pygame.K_e:
                        aposta="e"
                        quantidade=10
                        while ok:
                            cavalinho63_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_e:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=0
                    elif event.key==pygame.K_r:
                        aposta="r"
                        quantidade=10
                        while ok:
                            cavalinho64_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_r:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=0
                    elif event.key==pygame.K_t:
                        aposta="t"
                        quantidade=10
                        while ok:
                            cavalinho65_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_t:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=0
                    elif event.key==pygame.K_y:
                        aposta="y"
                        quantidade=10
                        while ok:
                            cavalinho66_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_y:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=0
                    elif event.key==pygame.K_SPACE:
                        ok=False
                        vez=0
                        comeco=False
                        aposta="x"
                        quantidade=1
    
        #mudanças no jogador 6
        J6.aposta(aposta, quantidade)
        J6.ganha_grana(-quantidade)

        tela.blit(font1.render(str(J1.carteira), True, (0, 0, 0)), (40,40))
        tela.blit(font1.render(str(J2.carteira), True, (0, 0, 0)), (180,40))  
        tela.blit(font1.render(str(J3.carteira), True, (0, 0, 0)), (320,40))  
        tela.blit(font1.render(str(J4.carteira), True, (0, 0, 0)), (460,40))  
        tela.blit(font1.render(str(J5.carteira), True, (0, 0, 0)), (600,40))  
        tela.blit(font1.render(str(J6.carteira), True, (0, 0, 0)), (740,40))  

    if largada:
        if cont == 0:
            text1 = '5'
            tela.blit(font.render(text1, True, (0, 0, 0)), (700,400))
            pygame.display.update()
        elif cont == 30:
            text2 = '4'
            tela.blit(font.render(text2, True, (0, 0, 0)), (700,400))
            pygame.display.update()
        elif cont == 60:
            text3 = '3'
            tela.blit(font.render(text3, True, (0, 0, 0)), (700,400))
            pygame.display.update()
        elif cont == 90:
            text4 = '2'
            tela.blit(font.render(text4, True, (0, 0, 0)), (700,400))
            pygame.display.update()
        elif cont == 120:
            text5 = '1'
            tela.blit(font.render(text5, True, (0, 0, 0)), (700,400))
            pygame.display.update()
        elif cont == 150:
            text6 = 'GO!!!'
            tela.blit(font.render(text6, True, (0, 0, 0)), (700,400))
            pygame.display.update()
            largada= False
        cont += 1
        
  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:      
            rodando = False
            
  #cavalinhos correm
    if not largada:
        if v > -3400:
            if cavalinho1.vx > cavalinho2.vx and cavalinho1.vx > cavalinho3.vx and cavalinho1.vx > cavalinho4.vx and cavalinho1.vx > cavalinho5.vx and cavalinho1.vx > cavalinho6.vx:
                v += -cavalinho1.max * 4.4
            if cavalinho2.vx > cavalinho1.vx and cavalinho2.vx > cavalinho3.vx and cavalinho2.vx > cavalinho4.vx and cavalinho2.vx > cavalinho5.vx and cavalinho2.vx > cavalinho6.vx:
                v += -cavalinho2.max * 4.4
            if cavalinho3.vx > cavalinho1.vx and cavalinho3.vx > cavalinho2.vx and cavalinho3.vx > cavalinho4.vx and cavalinho3.vx > cavalinho5.vx and cavalinho3.vx > cavalinho6.vx:
                v += -cavalinho3.max * 4.4
            if cavalinho4.vx > cavalinho1.vx and cavalinho4.vx > cavalinho2.vx and cavalinho4.vx > cavalinho3.vx and cavalinho4.vx > cavalinho5.vx and cavalinho4.vx > cavalinho6.vx:
                v += -cavalinho4.max * 4.4
            if cavalinho5.vx > cavalinho1.vx and cavalinho5.vx > cavalinho2.vx and cavalinho5.vx > cavalinho3.vx and cavalinho5.vx > cavalinho4.vx and cavalinho5.vx > cavalinho6.vx:
                v += -cavalinho5.max * 4.4
            if cavalinho6.vx > cavalinho1.vx and cavalinho6.vx > cavalinho2.vx and cavalinho6.vx > cavalinho3.vx and cavalinho6.vx > cavalinho4.vx and cavalinho6.vx > cavalinho5.vx:
                v += -cavalinho6.max * 4.4
        
        tela.blit(font1.render(str(J1.carteira), True, (0, 0, 0)), (40,40))
        tela.blit(font1.render(str(J2.carteira), True, (0, 0, 0)), (180,40))      
        pygame.display.update()

        movimento (cavalinho1,cavalinho2,cavalinho3,cavalinho4,cavalinho5,cavalinho6)

          
  #gera saídas
    tela.blit(fundo, (v, 0))
    cavalinho1_group.draw(tela)
    cavalinho2_group.draw(tela)
    cavalinho3_group.draw(tela)
    cavalinho4_group.draw(tela)
    cavalinho5_group.draw(tela)
    cavalinho6_group.draw(tela)
    
   #testa se o cavalinho da escolha ganhou, e gera uma mensagem com a resposta na tela
    if cav_escolha[cavalinho1]==J1.aposta and cavalinho1.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho2]==J1.aposta and cavalinho2.rect.x>=linha:
        if cavalinho1.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho3]==J1.aposta and cavalinho3.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho1.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho4]==J1.aposta and cavalinho4.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho1.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho5]==J1.aposta and cavalinho5.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho1.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho6]==J1.aposta and cavalinho6.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho1.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
            
    if cav_escolha[cavalinho1]==J1.aposta and cavalinho1.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho2]==J1.aposta and cavalinho2.rect.x>=linha:
        if cavalinho1.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho3]==J1.aposta and cavalinho3.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho1.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho4]==J1.aposta and cavalinho4.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho1.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho5]==J1.aposta and cavalinho5.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho1.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho6]==J1.aposta and cavalinho6.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho1.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False

    if cav_escolha[cavalinho1]==J1.aposta and cavalinho1.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho2]==J1.aposta and cavalinho2.rect.x>=linha:
        if cavalinho1.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho3]==J1.aposta and cavalinho3.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho1.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho4]==J1.aposta and cavalinho4.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho1.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho5]==J1.aposta and cavalinho5.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho1.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho6]==J1.aposta and cavalinho6.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho1.rect.x<linha:
            J1.ganha_grana(J1.quantidade*2)
            acaba=False
            
    if cav_escolha[cavalinho1]==J5.aposta and cavalinho1.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J5.ganha_grana(J5.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho2]==J5.aposta and cavalinho2.rect.x>=linha:
        if cavalinho1.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J5.ganha_grana(J5.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho3]==J5.aposta and cavalinho3.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho1.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J5.ganha_grana(J5.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho4]==J5.aposta and cavalinho4.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho1.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J5.ganha_grana(J5.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho5]==J5.aposta and cavalinho5.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho1.rect.x<linha and cavalinho6.rect.x<linha:
            J5.ganha_grana(J5.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho6]==J5.aposta and cavalinho6.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho1.rect.x<linha:
            J5.ganha_grana(J5.quantidade*2)
            acaba=False
            
    if cav_escolha[cavalinho1]==J6.aposta and cavalinho1.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J6.ganha_grana(J6.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho2]==J6.aposta and cavalinho2.rect.x>=linha:
        if cavalinho1.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J6.ganha_grana(J6.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho3]==J6.aposta and cavalinho3.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho1.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J6.ganha_grana(J6.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho4]==J6.aposta and cavalinho4.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho1.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J6.ganha_grana(J6.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho5]==J6.aposta and cavalinho5.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho1.rect.x<linha and cavalinho6.rect.x<linha:
            J6.ganha_grana(J6.quantidade*2)
            acaba=False
    elif cav_escolha[cavalinho6]==J6.aposta and cavalinho6.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho1.rect.x<linha:
            J6.ganha_grana(J6.quantidade*2)
            acaba=False
            
            

            
    tela.blit(font1.render(str(J1.carteira), True, (0, 0, 0)), (40,40))
    tela.blit(font1.render(str(J2.carteira), True, (0, 0, 0)), (180,40))      
    pygame.display.update()

                    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:      
            rodando = False
            
    if not largada:
        pygame.display.update()      #coloca a tela na janela
        
            
pygame.display.quit()