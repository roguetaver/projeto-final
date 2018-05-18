# -*- coding: utf-8 -*-
"""
Created on Thu May 17 18:13:36 2018

@author: andre
"""



from classecavalinho1 import Cavalinho
import pygame
from pygame.locals import *
from random import randrange
from classebotao import botao
from classemensagem import mensagem
from funcaomov import movimento

# ===============   INICIALIZAÇÃO   ===============
pygame.init()
w, h = 1400, 1000
hw = w/2
hh = h/2
area = w * h
tela = pygame.display.set_mode((w, h))
FPS = 120
pygame.display.set_caption('TURFE')


 
# carrega imagem de fundo 
fundo = pygame.image.load("fundo.png")
fundo = pygame.transform.scale(fundo,(5000,800))

v = 0
v1 = 0
font = pygame.font.SysFont('Consolas', 80)
clock = pygame.time.Clock()
init = True 
init1 = True
escolha="errado"
escolha1 = 'errado'
linha = 900

rodando=True
acaba= True
acaba1 = True
ganhou = False
ganhou1 = False
perdeu = False
perdeu1 = False
cont = 0
cont1 = 0
comeco = True
comeco1 = True

#blocos de repetição
bloco1 = True
bloco2 = False
   
# ===============   LOOPING PRINCIPAL   ===============

#loop
while rodando:
    while bloco1:
        clock.tick(FPS)
        
        while comeco:
            
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
            derrota = mensagem("derrota.png",400,100)
            derrota_group = pygame.sprite.Group()
            derrota_group.add(derrota)
            
            parabens = mensagem("parabens.png",400,100)
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
        
            #escolha do jogador
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
                    comeco = False
        
        if init:
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
                init = False
            cont += 1
            
      
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:      
                rodando = False
                
      #cavalinhos correm
        if not init:
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
        if cav_escolha[cavalinho1]==escolha and cavalinho1.rect.x>=linha:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                ganhou = True
                acaba=False
        elif cav_escolha[cavalinho2]==escolha and cavalinho2.rect.x>=linha:
            if cavalinho1.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                ganhou = True
                acaba=False
        elif cav_escolha[cavalinho3]==escolha and cavalinho3.rect.x>=linha:
            if cavalinho2.rect.x<linha and cavalinho1.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                ganhou = True
                acaba=False
        elif cav_escolha[cavalinho4]==escolha and cavalinho4.rect.x>=linha:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho1.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                ganhou = True
                acaba=False
        elif cav_escolha[cavalinho5]==escolha and cavalinho5.rect.x>=linha:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho1.rect.x<linha and cavalinho6.rect.x<linha:
                ganhou = True
                acaba=False
        elif cav_escolha[cavalinho6]==escolha and cavalinho6.rect.x>=linha:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho1.rect.x<linha:
                ganhou = True
                acaba=False
        elif cavalinho1.rect.x >= linha or cavalinho2.rect.x >= linha or cavalinho3.rect.x >= linha or cavalinho4.rect.x >= linha or cavalinho5.rect.x >= linha or cavalinho6.rect.x >= linha:
            if acaba:
                perdeu = True
        if perdeu:
            derrota_group.draw(tela)
            continuar = 'APERTE ESPAÇO PARA CONTINUAR'
            tela.blit(font.render(continuar, True, (0, 0, 0)), (5,600))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bloco1 = False
                        bloco2 = True
                        v1=0
                        ganhou1 = False
                        perdeu1=False
                        acaba1 = True
                        cont1 = 0
                        init1 = True 
                        escolha1="errado"
                        comeco1=True
        if ganhou:
            parabens_group.draw(tela)
            continuar = 'APERTE ESPAÇO PARA CONTINUAR'
            tela.blit(font.render(continuar, True, (0, 0, 0)), (5,600))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bloco1 = False
                        bloco2 = True
                        v1=0
                        ganhou1 = False
                        perdeu1=False
                        acaba1 = True
                        cont1 = 0
                        init1 = True 
                        escolha1="errado"
                        comeco1=True
        if not init:
            pygame.display.update()      #coloca a tela na janela
            
            
     #bloco2       
    while bloco2:
        clock.tick(FPS)
        
        while comeco1:
            
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
            derrota = mensagem("derrota.png",400,100)
            derrota_group = pygame.sprite.Group()
            derrota_group.add(derrota)
            
            parabens = mensagem("parabens.png",400,100)
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
        
            #escolha do jogador
            while escolha1=="errado":
                for event in pygame.event.get():
                    if event.type==pygame.KEYUP:
                        if event.key==pygame.K_q:
                            escolha1="q"
                        elif event.key==pygame.K_w:
                            escolha1="w"
                        elif event.key==pygame.K_e:
                            escolha1="e"
                        elif event.key==pygame.K_r:
                            escolha1="r"
                        elif event.key==pygame.K_t:
                            escolha1="t"
                        elif event.key==pygame.K_y:
                            escolha1="y"
                    comeco1 = False
        
        if init1:
            if cont1 == 0:
                text1 = '5'
                tela.blit(font.render(text1, True, (0, 0, 0)), (700,400))
                pygame.display.update()
            elif cont1 == 30:
                text2 = '4'
                tela.blit(font.render(text2, True, (0, 0, 0)), (700,400))
                pygame.display.update()
            elif cont1 == 60:
                text3 = '3'
                tela.blit(font.render(text3, True, (0, 0, 0)), (700,400))
                pygame.display.update()
            elif cont1 == 90:
                text4 = '2'
                tela.blit(font.render(text4, True, (0, 0, 0)), (700,400))
                pygame.display.update()
            elif cont1 == 120:
                text5 = '1'
                tela.blit(font.render(text5, True, (0, 0, 0)), (700,400))
                pygame.display.update()
            elif cont1 == 150:
                text6 = 'GO!!!'
                tela.blit(font.render(text6, True, (0, 0, 0)), (700,400))
                pygame.display.update()
                init1 = False
            cont1 += 1
            
      
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:      
                rodando = False
                
      #cavalinhos correm
        if not init1:
            if v1 > -3400:
                if cavalinho1.vx > cavalinho2.vx and cavalinho1.vx > cavalinho3.vx and cavalinho1.vx > cavalinho4.vx and cavalinho1.vx > cavalinho5.vx and cavalinho1.vx > cavalinho6.vx:
                    v1 += -cavalinho1.max * 4.4
                if cavalinho2.vx > cavalinho1.vx and cavalinho2.vx > cavalinho3.vx and cavalinho2.vx > cavalinho4.vx and cavalinho2.vx > cavalinho5.vx and cavalinho2.vx > cavalinho6.vx:
                    v1 += -cavalinho2.max * 4.4
                if cavalinho3.vx > cavalinho1.vx and cavalinho3.vx > cavalinho2.vx and cavalinho3.vx > cavalinho4.vx and cavalinho3.vx > cavalinho5.vx and cavalinho3.vx > cavalinho6.vx:
                    v1 += -cavalinho3.max * 4.4
                if cavalinho4.vx > cavalinho1.vx and cavalinho4.vx > cavalinho2.vx and cavalinho4.vx > cavalinho3.vx and cavalinho4.vx > cavalinho5.vx and cavalinho4.vx > cavalinho6.vx:
                    v1 += -cavalinho4.max * 4.4
                if cavalinho5.vx > cavalinho1.vx and cavalinho5.vx > cavalinho2.vx and cavalinho5.vx > cavalinho3.vx and cavalinho5.vx > cavalinho4.vx and cavalinho5.vx > cavalinho6.vx:
                    v1 += -cavalinho5.max * 4.4
                if cavalinho6.vx > cavalinho1.vx and cavalinho6.vx > cavalinho2.vx and cavalinho6.vx > cavalinho3.vx and cavalinho6.vx > cavalinho4.vx and cavalinho6.vx > cavalinho5.vx:
                    v1 += -cavalinho6.max * 4.4
            
            
    
            movimento (cavalinho1,cavalinho2,cavalinho3,cavalinho4,cavalinho5,cavalinho6)
    
              
      #gera saídas
        tela.blit(fundo, (v1, 0))
        cavalinho1_group.draw(tela)
        cavalinho2_group.draw(tela)
        cavalinho3_group.draw(tela)
        cavalinho4_group.draw(tela)
        cavalinho5_group.draw(tela)
        cavalinho6_group.draw(tela)
        
       #testa se o cavalinho da escolha ganhou, e gera uma mensagem com a resposta na tela
        if cav_escolha[cavalinho1]==escolha1 and cavalinho1.rect.x>=linha:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                ganhou1 = True
                acaba1=False
        elif cav_escolha[cavalinho2]==escolha1 and cavalinho2.rect.x>=linha:
            if cavalinho1.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                ganhou1 = True
                acaba1=False
        elif cav_escolha[cavalinho3]==escolha1 and cavalinho3.rect.x>=linha:
            if cavalinho2.rect.x<linha and cavalinho1.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                ganhou1 = True
                acaba1=False
        elif cav_escolha[cavalinho4]==escolha1 and cavalinho4.rect.x>=linha:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho1.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                ganhou1 = True
                acaba1=False
        elif cav_escolha[cavalinho5]==escolha1 and cavalinho5.rect.x>=linha:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho1.rect.x<linha and cavalinho6.rect.x<linha:
                ganhou1 = True
                acaba1=False
        elif cav_escolha[cavalinho6]==escolha1 and cavalinho6.rect.x>=linha:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho1.rect.x<linha:
                ganhou1 = True
                acaba1=False
        elif cavalinho1.rect.x >= linha or cavalinho2.rect.x >= linha or cavalinho3.rect.x >= linha or cavalinho4.rect.x >= linha or cavalinho5.rect.x >= linha or cavalinho6.rect.x >= linha:
            if acaba1:
                perdeu1 = True
        if perdeu1:
            derrota_group.draw(tela)
            continuar = 'APERTE ESPAÇO PARA CONTINUAR'
            tela.blit(font.render(continuar, True, (0, 0, 0)), (5,600))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bloco2 = False
                        bloco1 = True
                        v=0
                        ganhou = False
                        perdeu=False
                        acaba = True
                        cont = 0
                        init = True 
                        escolha="errado"
                        comeco=True
        if ganhou1:
            parabens_group.draw(tela)
            continuar = 'APERTE ESPAÇO PARA CONTINUAR'
            tela.blit(font.render(continuar, True, (0, 0, 0)), (5,600))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bloco2 = False
                        bloco1 = True
                        v=0
                        ganhou = False
                        perdeu=False
                        acaba = True
                        cont = 0
                        init = True 
                        escolha="errado"
                        comeco=True
                                                
        if not init1:
            pygame.display.update()      #coloca a tela na janela
        


    
pygame.display.quit()