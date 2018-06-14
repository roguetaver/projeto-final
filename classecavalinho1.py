# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:56:43 2018

@author: andre
"""

import pygame

class Cavalinho(pygame.sprite.Sprite):
  
  def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x, aceleracao, velocidade_max):
    pygame.sprite.Sprite.__init__(self)
    self.vx = vel_x
    imagem=pygame.image.load(arquivo_imagem)
    self.image = pygame.transform.scale(imagem,(220,160))
    self.rect = self.image.get_rect()
    self.rect.x = pos_x
    self.rect.y = pos_y
    self.aceleracao=aceleracao
    self.max= velocidade_max
    
  def move(self):
    self.rect.x += self.vx
    
  def acelera(self):
    self.vx += self.aceleracao
    
  def correndo (self):
      
    self.move()
    if self.vx<=self.max: 
        self.acelera()