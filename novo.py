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

# ===============   INICIALIZAÇÃO   ===============
pygame.init()
largura, altura = 1400, 1000
hw = largura/2
hh = altura/2
area = largura * altura
tela = pygame.display.set_mode((largura, altura))
FPS = 120
pygame.display.set_caption('TURFE')


 
# carrega imagem de fundo 
fundo = pygame.image.load("pistamov.png")
fundo = pygame.transform.scale(fundo,(5000,800))

v = 0
font = pygame.font.SysFont('Consolas', 80)
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
cavalinho1 = Cavalinho("cavalinho1.png",10,100, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
cavalinho1_group = pygame.sprite.Group()
cavalinho1_group.add(cavalinho1)

cavalinho2 = Cavalinho("cavalinho2.png",10,210, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
cavalinho2_group = pygame.sprite.Group()
cavalinho2_group.add(cavalinho2)

cavalinho3 = Cavalinho("cavalinho3.png",10,320, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
cavalinho3_group = pygame.sprite.Group()
cavalinho3_group.add(cavalinho3)

cavalinho4 = Cavalinho("cavalinho4.png",10,440, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
cavalinho4_group = pygame.sprite.Group()
cavalinho4_group.add(cavalinho4)

cavalinho5 = Cavalinho("cavalinho5.png",10,550, 
            randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
cavalinho5_group = pygame.sprite.Group()
cavalinho5_group.add(cavalinho5)

cavalinho6 = Cavalinho("cavalinho6.png",10,660, 
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
Q = botao("Q.png",130,120)
Q_group = pygame.sprite.Group()
Q_group.add(Q)

W = botao("W.png",130,230)
W_group = pygame.sprite.Group()
W_group.add(W)

E = botao("E.png",130,350)
E_group = pygame.sprite.Group()
E_group.add(E)

R = botao("R.png",130,460)
R_group = pygame.sprite.Group()
R_group.add(R)

T = botao("T.png",130,570)
T_group = pygame.sprite.Group()
T_group.add(T)

Y = botao("Y.png",130,680)
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

p1 = mensagem("p1.png",10,10, 130, 110)
p1_group = pygame.sprite.Group()
p1_group.add(p1)

p2 = mensagem("p2.png",150,10, 130, 110)
p2_group = pygame.sprite.Group()
p2_group.add(p2)

#criar jogadores
J1 = jogador("jogador 1", 100)
J1_group = pygame.sprite.Group()
J1_group.add(J1)
   
J2 = jogador("jogador 2", 100)
J2_group = pygame.sprite.Group()
J2_group.add(J2)
# ===============   LOOPING PRINCIPAL   ===============

#loop
while rodando:
    clock.tick(60)
    
    while comeco:    
        
        #gerar tela do jogo inicial
        tela.blit(fundo, (0, 0))
        p1_group.draw(tela)
        p2_group.draw(tela)
        cavalinho1_group.draw(tela)
        cavalinho2_group.draw(tela)
        cavalinho3_group.draw(tela)
        cavalinho4_group.draw(tela)
        cavalinho5_group.draw(tela)
        cavalinho6_group.draw(tela)
        tela.blit(font.render(str(J1.carteira), True, (0, 0, 0)), (50,10))
        tela.blit(font.render(str(J2.carteira), True, (0, 0, 0)), (200,10))      
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

        tela.blit(font.render("Jogador {0}, escolha o seu cavalo".format(vez), True, (0, 0, 0)), (5,300))
        pygame.display.update()
        #escolha do jogador 1
        while vez == 1:
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
                                        comeco=False
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
                                        comeco=False
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
                                        comeco=False
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
                                        comeco=False
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
                                        comeco=False
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
                                        comeco=False
                                        vez=2
                    elif event.key==pygame.K_SPACE:
                        ok=False
                        vez=2
                        comeco=False
                        aposta=0
                        quantidade=1
        
        #mudanças no jogador 1
        J1.aposta(aposta, quantidade)
        J1.ganha_grana(-quantidade)
        i=2
        tela.blit(font.render("Jogador {0}, escolha o seu cavalo".format(vez), True, (0, 0, 0)), (5,300))
        pygame.display.update()
        #escolha do jogador 2
        while vez == 2:
             for event in pygame.event.get():
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_q:
                        aposta="q"
                        quantidade=10
                        while ok:
                            cavalinho21_group.draw(tela)
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
                            cavalinho22_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=0
                    elif event.key==pygame.K_e:
                        aposta="e"
                        quantidade=10
                        while ok:
                            cavalinho23_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=0
                    elif event.key==pygame.K_r:
                        aposta="r"
                        quantidade=10
                        while ok:
                            cavalinho24_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=0
                    elif event.key==pygame.K_t:
                        aposta="t"
                        quantidade=10
                        while ok:
                            cavalinho25_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=0
                    elif event.key==pygame.K_y:
                        aposta="y"
                        quantidade=10
                        while ok:
                            cavalinho26_group.draw(tela)
                            for event in pygame.event.get():
                                if event.type==pygame.KEYUP:       
                                    if event.key==pygame.K_q:
                                        quantidade+=10
                                    elif event.key==pygame.K_SPACE:
                                        ok=False
                                        comeco=False
                                        vez=0
                    elif event.key==pygame.K_SPACE:
                        ok=False
                        vez=0
                        comeco=False
                        aposta=0
                        quantidade=1
                        
        #mudanças no jogador 2
        J2.aposta(aposta, quantidade)
        J2.ganha_grana(-quantidade)
        
        tela.blit(font.render(str(J1.carteira), True, (0, 0, 0)), (50,10))
        tela.blit(font.render(str(J2.carteira), True, (0, 0, 0)), (200,10))      
        pygame.display.update()
                
            
    
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
        
        tela.blit(font.render(str(J1.carteira), True, (0, 0, 0)), (50,10))
        tela.blit(font.render(str(J2.carteira), True, (0, 0, 0)), (200,10))      
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
            J1.ganha_grana(J1.aposta*2)
            acaba=False
    elif cav_escolha[cavalinho2]==J1.aposta and cavalinho2.rect.x>=linha:
        if cavalinho1.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.aposta*2)
            acaba=False
    elif cav_escolha[cavalinho3]==J1.aposta and cavalinho3.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho1.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.aposta*2)
            acaba=False
    elif cav_escolha[cavalinho4]==J1.aposta and cavalinho4.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho1.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.aposta*2)
            acaba=False
    elif cav_escolha[cavalinho5]==J1.aposta and cavalinho5.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho1.rect.x<linha and cavalinho6.rect.x<linha:
            J1.ganha_grana(J1.aposta*2)
            acaba=False
    elif cav_escolha[cavalinho6]==J1.aposta and cavalinho6.rect.x>=linha:
        if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho1.rect.x<linha:
            J1.ganha_grana(J1.aposta*2)
            acaba=False
    elif cavalinho1.rect.x >= linha or cavalinho2.rect.x >= linha or cavalinho3.rect.x >= linha or cavalinho4.rect.x >= linha or cavalinho5.rect.x >= linha or cavalinho6.rect.x >= linha:
        if acaba:
            perdeu = True
            
    tela.blit(font.render(str(J1.carteira), True, (0, 0, 0)), (50,10))
    tela.blit(font.render(str(J2.carteira), True, (0, 0, 0)), (200,10))      
    pygame.display.update()

                    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:      
            rodando = False
            
    if not largada:
        pygame.display.update()      #coloca a tela na janela
        
            
pygame.display.quit()