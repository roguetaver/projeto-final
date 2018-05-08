# -*- coding: utf-8 -*-
"""
Created on Mon May  7 21:45:36 2018
pygame.KEYUP and e.key == pygame.K_SPACE
@author: andre
"""

import pygame 


def largada (tela,fundo):
    counter, text = 5, '5'.rjust(3)
    tela.blit(fundo, (0, 0))
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 80)
    clock = pygame.time.Clock()
    init = True 
    while init:
        for e in pygame.event.get():
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                    counter -= 1
                    text = str(counter).rjust(3) if counter > 0 else 'GO!!!!'
                    if text == 'GO!!!!':
                        init = False
                    if e.type == pygame.QUIT: break
            else:
                tela.blit(fundo, (0, 0))
                tela.blit(font.render(text, True, (0, 0, 0)), (500,300))
                pygame.display.update()
                clock.tick(60)
                continue
            
