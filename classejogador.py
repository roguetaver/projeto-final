# -*- coding: utf-8 -*-
"""
Created on Fri May 11 09:00:02 2018

@author: mihan
"""
import pygame

class jogador(pygame.sprite.Sprite):
    
    def __init__(self, nome, saldo_inicial):
        pygame.sprite.Sprite.__init__(self)
        self.carteira=saldo_inicial
        self.nome = nome
        
    def ganha_grana(self, mudanca):
        self.carteira+=mudanca
        
    def aposta(self, escolha, vezes):
        self.aposta = escolha
        self.quantidade = vezes