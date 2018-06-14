# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:05:50 2018

@author: andre
"""

import pygame

class mensagem(pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        imagem=pygame.image.load(arquivo_imagem)
        self.image = pygame.transform.scale(imagem,(600,600))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y