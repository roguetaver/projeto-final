# -*- coding: utf-8 -*-
"""
Created on Thu May  3 13:57:33 2018

@author: mihan
"""

from cavalinho import Cavalinho
import pygame
import sys
from pygame.locals import *
from random import randrange
 
# ===============   INICIALIZAÇÃO   ===============
pygame.init()
tela = pygame.display.set_mode((1200, 680), 0, 32)
pygame.display.set_caption('Horse Power')
 
# carrega imagem de fundo (https://wallpapersafari.com/dark-green-background/)
fundo = pygame.image.load("pista.png")
fundo = pygame.transform.scale(fundo,(1200,660))
 
# cria cavalos
cavalinho1 = Cavalinho("cavalinho1.png",10,-20, 
            randrange(2,9))
cavalinho1_group = pygame.sprite.Group()
cavalinho1_group.add(cavalinho1)

cavalinho2 = Cavalinho("cavalinho2.png",10,90, 
            randrange(2,9))
cavalinho2_group = pygame.sprite.Group()
cavalinho2_group.add(cavalinho2)

cavalinho3 = Cavalinho("cavalinho3.png",10,200, 
            randrange(2,9))
cavalinho3_group = pygame.sprite.Group()
cavalinho3_group.add(cavalinho3)

cavalinho4 = Cavalinho("cavalinho4.png",10,310, 
            randrange(2,9))
cavalinho4_group = pygame.sprite.Group()
cavalinho4_group.add(cavalinho4)

cavalinho5 = Cavalinho("cavalinho5.png",10,420, 
            randrange(2,9))
cavalinho5_group = pygame.sprite.Group()
cavalinho5_group.add(cavalinho5)

cavalinho6 = Cavalinho("cavalinho6.png",10,530, 
            randrange(2,9))
cavalinho6_group = pygame.sprite.Group()
cavalinho6_group.add(cavalinho6)

# ===============   LOOPING PRINCIPAL   ===============
rodando = True
while rodando:
  
  for event in pygame.event.get():  #pega lista de eventos
    if event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
      rodando = False            #executa a função de sistema "exit"
  #move a bola pela tela
  cavalinho1.move()
  if cavalinho1.rect.x < 10:
    cavalinho1.vx = cavalinho1.vx
    
  cavalinho2.move()
  if cavalinho2.rect.x < 10:
    cavalinho2.vx = cavalinho2.vx
    
  cavalinho3.move()
  if cavalinho3.rect.x < 10:
    cavalinho3.vx = cavalinho3.vx
    
  cavalinho4.move()
  if cavalinho4.rect.x < 10:
    cavalinho4.vx = cavalinho4.vx
    
  cavalinho5.move()
  if cavalinho5.rect.x < 10:
    cavalinho5.vx = cavalinho5.vx
    
  cavalinho6.move()
  if cavalinho6.rect.x < 10:
    cavalinho6.vx = cavalinho6.vx
        
  #gera saídas
  tela.blit(fundo, (0, 0))
  cavalinho1_group.draw(tela)
  cavalinho2_group.draw(tela)
  cavalinho3_group.draw(tela)
  cavalinho4_group.draw(tela)
  cavalinho5_group.draw(tela)
  cavalinho6_group.draw(tela)
  pygame.display.update()      #coloca a tela na janela
    
pygame.display.quit()