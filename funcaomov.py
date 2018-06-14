# -*- coding: utf-8 -*-
"""
Created on Mon May  7 00:31:53 2018

@author: andre
"""

def movimento (cavalinho1,cavalinho2,cavalinho3,cavalinho4,cavalinho5,cavalinho6):
    if cavalinho1.rect.x < 1465:
        cavalinho1.correndo()
    
    if cavalinho2.rect.x < 1465:
        cavalinho2.correndo()
    
    if cavalinho3.rect.x < 1465:
        cavalinho3.correndo()
        
    if cavalinho4.rect.x < 1465:
        cavalinho4.correndo()
    
    if cavalinho5.rect.x < 1465:
        cavalinho5.correndo()
    
    if cavalinho6.rect.x < 1465:
        cavalinho6.correndo()