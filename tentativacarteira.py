# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 22:49:04 2018

@author: andre
"""



from classecavalinho1 import Cavalinho
import pygame
from pygame.locals import *
from random import randrange
from classebotao import botao
from classemensagem import mensagem
from funcaomov import movimento
from classemensagemp import mensagemp


# ===============   INICIALIZAÇÃO   ===============
pygame.init()
w, h = 1100, 650
hw = w/2
hh = h/2
area = w * h
tela = pygame.display.set_mode((w, h))
FPS = 30
pygame.display.set_caption('TURFE')


 
# carrega imagem de fundo 
fundo = pygame.image.load("fundo.png")
fundo = pygame.transform.scale(fundo,(5000,h))


v = 0
v1 = 0
font = pygame.font.SysFont('Consolas', 80)
font1 = pygame.font.SysFont('Consolas', 25)
font2 = pygame.font.SysFont('Consolas', 35)
clock = pygame.time.Clock()
init = True 
init1 = True
linha = 800
rodando=True
acaba= False
acaba1 = False

perdeu = False
perdeu1 = False
cont = 0
cont1 = 0
comeco = True
comeco1 = True
chegada = True
chegada1 = True

#blocos de repetição
bloco1 = True
bloco2 = False
carteira1 = 100
carteira2 = 100
carteira3 = 100
carteira4 = 100
carteira5 = 100
carteira6 = 100


   
# ===============   LOOPING PRINCIPAL   ===============

#loop
while rodando:
    while bloco1:
        
        clock.tick(FPS)
        
        while comeco:
            
                # cria cavalos
            cavalinho1 = Cavalinho("cavalinho1.png",10,85, 
                        randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
            cavalinho1_group = pygame.sprite.Group()
            cavalinho1_group.add(cavalinho1)
            
            cavalinho2 = Cavalinho("cavalinho2.png",10,195, 
                        randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
            cavalinho2_group = pygame.sprite.Group()
            cavalinho2_group.add(cavalinho2)
            
            cavalinho3 = Cavalinho("cavalinho3.png",10,305, 
                        randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
            cavalinho3_group = pygame.sprite.Group()
            cavalinho3_group.add(cavalinho3)
            
            cavalinho4 = Cavalinho("cavalinho4.png",10,415, 
                        randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
            cavalinho4_group = pygame.sprite.Group()
            cavalinho4_group.add(cavalinho4)
            
            cavalinho5 = Cavalinho("cavalinho5.png",10,535, 
                        randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
            cavalinho5_group = pygame.sprite.Group()
            cavalinho5_group.add(cavalinho5)
            
            cavalinho6 = Cavalinho("cavalinho6.png",10,645, 
                        randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
            cavalinho6_group = pygame.sprite.Group()
            cavalinho6_group.add(cavalinho6)
            
            
            
            p1 = mensagemp("p1.png",10,10, 130, 87)
            p1_group = pygame.sprite.Group()
            p1_group.add(p1)

            p2 = mensagemp("p2.png",150,10, 130, 87)
            p2_group = pygame.sprite.Group()
            p2_group.add(p2)

            p3 = mensagemp("p3.png",290,10, 130, 87)
            p3_group = pygame.sprite.Group()
            p3_group.add(p3)

            p4 = mensagemp("p4.png",430,10, 130, 87)
            p4_group = pygame.sprite.Group()
            p4_group.add(p4)

            p5 = mensagemp("p5.png",570,10, 130, 87)
            p5_group = pygame.sprite.Group()
            p5_group.add(p5)
        
            p6 = mensagemp("p6.png",710,10, 130, 87)
            p6_group = pygame.sprite.Group()
            p6_group.add(p6)
            


            
            #gerar tela do jogo inicial
            tela.blit(fundo, (0, 0))
            cavalinho1_group.draw(tela)
            cavalinho2_group.draw(tela)
            cavalinho3_group.draw(tela)
            cavalinho4_group.draw(tela)
            cavalinho5_group.draw(tela)
            cavalinho6_group.draw(tela)
            p1_group.draw(tela)
            p2_group.draw(tela)
            p3_group.draw(tela)
            p4_group.draw(tela)
            p5_group.draw(tela)
            p6_group.draw(tela)
            tela.blit(font1.render(str(carteira1), True, (0, 0, 0)), (40,40))
            tela.blit(font1.render(str(carteira2), True, (0, 0, 0)), (180,40))
            tela.blit(font1.render(str(carteira3), True, (0, 0, 0)), (320,40))
            tela.blit(font1.render(str(carteira4), True, (0, 0, 0)), (460,40))
            tela.blit(font1.render(str(carteira5), True, (0, 0, 0)), (600,40))
            tela.blit(font1.render(str(carteira6), True, (0, 0, 0)), (740,40))
            pygame.display.update()      #coloca a tela na janela
            
            continuar = 'APERTE ESPAÇO PARA CONTINUAR'
            tela.blit(font2.render(continuar, True, (0, 0, 0)), (5,600))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
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
        p1_group.draw(tela)
        p2_group.draw(tela)
        p3_group.draw(tela)
        p4_group.draw(tela)
        p5_group.draw(tela)
        p6_group.draw(tela)
        tela.blit(font1.render(str(carteira1), True, (0, 0, 0)), (40,40))
        tela.blit(font1.render(str(carteira2), True, (0, 0, 0)), (180,40))
        tela.blit(font1.render(str(carteira3), True, (0, 0, 0)), (320,40))
        tela.blit(font1.render(str(carteira4), True, (0, 0, 0)), (460,40))
        tela.blit(font1.render(str(carteira5), True, (0, 0, 0)), (600,40))
        tela.blit(font1.render(str(carteira6), True, (0, 0, 0)), (740,40))

       #testa se o cavalinho da escolha ganhou, e gera uma mensagem com a resposta na tela
        if cavalinho1.rect.x>=linha and chegada:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                carteira1 += 60
                carteira2 -= 10
                carteira3 -= 10
                carteira4 -= 10
                carteira5 -= 10
                carteira6 -= 10
                acaba = True
                chegada = False
                
                
        elif  cavalinho2.rect.x>=linha and chegada:
            if cavalinho1.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                carteira2 += 60
                carteira1 -= 10
                carteira3 -= 10
                carteira4 -= 10
                carteira5 -= 10
                carteira6 -= 10
                acaba = True
                chegada = False
                
        elif  cavalinho3.rect.x>=linha and chegada:
            if cavalinho2.rect.x<linha and cavalinho1.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                carteira3 += 60
                carteira2 -= 10
                carteira1 -= 10
                carteira4 -= 10
                carteira5 -= 10
                carteira6 -= 10
                acaba = True
                chegada = False
                
        elif  cavalinho4.rect.x>=linha and chegada:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho1.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                carteira4 += 60
                carteira2 -= 10
                carteira3 -= 10
                carteira1 -= 10
                carteira5 -= 10
                carteira6 -= 10
                acaba = True
                chegada = False
                
        elif  cavalinho5.rect.x>=linha and chegada:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho1.rect.x<linha and cavalinho6.rect.x<linha:
                carteira5 += 60
                carteira2 -= 10
                carteira3 -= 10
                carteira4 -= 10
                carteira1 -= 10
                carteira6 -= 10
                acaba = True
                chegada = False
                
        elif  cavalinho6.rect.x>=linha and chegada:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho1.rect.x<linha:
                carteira6 += 60
                carteira2 -= 10
                carteira3 -= 10
                carteira4 -= 10
                carteira5 -= 10
                carteira1 -= 10
                acaba = True
                chegada = False
                
        
        
        if acaba:    
            continuar = 'APERTE ESPAÇO PARA CONTINUAR'
            tela.blit(font2.render(continuar, True, (0, 0, 0)), (5,600))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                            bloco2 = True
                            bloco1 = False
                            v1=0
                            ganhou1 = False
                            perdeu1=False
                            acaba1 = False
                            cont1 = 0
                            init1 = True 
                            escolha1="errado"
                            comeco1=True
                            chegada1 = True

        if not init:
            pygame.display.update()      #coloca a tela na janela
            
            
     #bloco2       
    while bloco2:
        clock.tick(FPS)
        
        while comeco1:
            
                
                # cria cavalos
            cavalinho1 = Cavalinho("cavalinho1.png",10,85, 
                        randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
            cavalinho1_group = pygame.sprite.Group()
            cavalinho1_group.add(cavalinho1)
            
            cavalinho2 = Cavalinho("cavalinho2.png",10,195, 
                        randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
            cavalinho2_group = pygame.sprite.Group()
            cavalinho2_group.add(cavalinho2)
            
            cavalinho3 = Cavalinho("cavalinho3.png",10,305, 
                        randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
            cavalinho3_group = pygame.sprite.Group()
            cavalinho3_group.add(cavalinho3)
            
            cavalinho4 = Cavalinho("cavalinho4.png",10,415, 
                        randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
            cavalinho4_group = pygame.sprite.Group()
            cavalinho4_group.add(cavalinho4)
            
            cavalinho5 = Cavalinho("cavalinho5.png",10,535, 
                        randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
            cavalinho5_group = pygame.sprite.Group()
            cavalinho5_group.add(cavalinho5)
            
            cavalinho6 = Cavalinho("cavalinho6.png",10,645, 
                        randrange(50,200)/100,randrange(5,30)/100, randrange(400,600)/100)
            cavalinho6_group = pygame.sprite.Group()
            cavalinho6_group.add(cavalinho6)
            
            
            
            p1 = mensagemp("p1.png",10,10, 130, 87)
            p1_group = pygame.sprite.Group()
            p1_group.add(p1)

            p2 = mensagemp("p2.png",150,10, 130, 87)
            p2_group = pygame.sprite.Group()
            p2_group.add(p2)

            p3 = mensagemp("p3.png",290,10, 130, 87)
            p3_group = pygame.sprite.Group()
            p3_group.add(p3)

            p4 = mensagemp("p4.png",430,10, 130, 87)
            p4_group = pygame.sprite.Group()
            p4_group.add(p4)

            p5 = mensagemp("p5.png",570,10, 130, 87)
            p5_group = pygame.sprite.Group()
            p5_group.add(p5)
        
            p6 = mensagemp("p6.png",710,10, 130, 87)
            p6_group = pygame.sprite.Group()
            p6_group.add(p6)
            


            
            #gerar tela do jogo inicial
            tela.blit(fundo, (0, 0))
            cavalinho1_group.draw(tela)
            cavalinho2_group.draw(tela)
            cavalinho3_group.draw(tela)
            cavalinho4_group.draw(tela)
            cavalinho5_group.draw(tela)
            cavalinho6_group.draw(tela)
            p1_group.draw(tela)
            p2_group.draw(tela)
            p3_group.draw(tela)
            p4_group.draw(tela)
            p5_group.draw(tela)
            p6_group.draw(tela)
            tela.blit(font1.render(str(carteira1), True, (0, 0, 0)), (40,40))
            tela.blit(font1.render(str(carteira2), True, (0, 0, 0)), (180,40))
            tela.blit(font1.render(str(carteira3), True, (0, 0, 0)), (320,40))
            tela.blit(font1.render(str(carteira4), True, (0, 0, 0)), (460,40))
            tela.blit(font1.render(str(carteira5), True, (0, 0, 0)), (600,40))
            tela.blit(font1.render(str(carteira6), True, (0, 0, 0)), (740,40))
            pygame.display.update()      #coloca a tela na janela
            
            continuar = 'APERTE ESPAÇO PARA CONTINUAR'
            tela.blit(font2.render(continuar, True, (0, 0, 0)), (5,600))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
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
        p1_group.draw(tela)
        p2_group.draw(tela)
        p3_group.draw(tela)
        p4_group.draw(tela)
        p5_group.draw(tela)
        p6_group.draw(tela)
        tela.blit(font1.render(str(carteira1), True, (0, 0, 0)), (40,40))
        tela.blit(font1.render(str(carteira2), True, (0, 0, 0)), (180,40))
        tela.blit(font1.render(str(carteira3), True, (0, 0, 0)), (320,40))
        tela.blit(font1.render(str(carteira4), True, (0, 0, 0)), (460,40))
        tela.blit(font1.render(str(carteira5), True, (0, 0, 0)), (600,40))
        tela.blit(font1.render(str(carteira6), True, (0, 0, 0)), (740,40))

       #testa se o cavalinho da escolha ganhou, e gera uma mensagem com a resposta na tela
        if cavalinho1.rect.x>=linha and chegada1:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                carteira1 += 60
                carteira2 -= 10
                carteira3 -= 10
                carteira4 -= 10
                carteira5 -= 10
                carteira6 -= 10
                acaba1 = True
                chegada1 = False
                
                
        elif  cavalinho2.rect.x>=linha and chegada1:
            if cavalinho1.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                carteira2 += 60
                carteira1 -= 10
                carteira3 -= 10
                carteira4 -= 10
                carteira5 -= 10
                carteira6 -= 10
                acaba1 = True
                chegada1 = False
                
        elif  cavalinho3.rect.x>=linha and chegada1:
            if cavalinho2.rect.x<linha and cavalinho1.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                carteira3 += 60
                carteira2 -= 10
                carteira1 -= 10
                carteira4 -= 10
                carteira5 -= 10
                carteira6 -= 10
                acaba1 = True
                chegada1 = False
                
        elif  cavalinho4.rect.x>=linha and chegada1:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho1.rect.x<linha and cavalinho5.rect.x<linha and cavalinho6.rect.x<linha:
                carteira4 += 60
                carteira2 -= 10
                carteira3 -= 10
                carteira1 -= 10
                carteira5 -= 10
                carteira6 -= 10
                acaba1 = True
                chegada1 = False
                
        elif  cavalinho5.rect.x>=linha and chegada1:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho1.rect.x<linha and cavalinho6.rect.x<linha:
                carteira5 += 60
                carteira2 -= 10
                carteira3 -= 10
                carteira4 -= 10
                carteira1 -= 10
                carteira6 -= 10
                acaba1 = True
                chegada1 = False
                
        elif  cavalinho6.rect.x>=linha and chegada1:
            if cavalinho2.rect.x<linha and cavalinho3.rect.x<linha and cavalinho4.rect.x<linha and cavalinho5.rect.x<linha and cavalinho1.rect.x<linha:
                carteira6 += 60
                carteira2 -= 10
                carteira3 -= 10
                carteira4 -= 10
                carteira5 -= 10
                carteira1 -= 10
                acaba1 = True
                chegada1 = False
                
        
        
        if acaba1:    
            continuar = 'APERTE ESPAÇO PARA CONTINUAR'
            tela.blit(font2.render(continuar, True, (0, 0, 0)), (5,600))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                            bloco2 = False
                            bloco1 = True
                            v=0
                            ganhou = False
                            perdeu=False
                            acaba = False
                            cont = 0
                            init = True 
                            escolha="errado"
                            comeco=True
                            chegada = True

        if not init1:
            pygame.display.update()      #coloca a tela na janela