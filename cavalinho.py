# -*- coding: utf-8 -*-
"""
Created on Thu May  3 13:26:42 2018

@author: mihan
"""
import pygame

class Cavalinho(pygame.sprite.Sprite):
  
  def __init__(self, arquivo_imagem, pos_x, pos_y, vel_x):
    pygame.sprite.Sprite.__init__(self)
    self.vx = vel_x
    imagem=pygame.image.load(arquivo_imagem)
    self.image = pygame.transform.scale(imagem,(193,133))
    self.rect = self.image.get_rect()
    self.rect.x = pos_x
    self.rect.y = pos_y
    
  def move(self):
    self.rect.x += self.vx
    