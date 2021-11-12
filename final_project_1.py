#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 11:15:16 2021

@author: abigailgreen
"""

import pygame
pygame.init()
display = pygame.display.set_mode((750,500))
WHITE = (255,255,255)
display.fill(WHITE)
FPS = 60

class Player:
    def __init__(self):
        self._location = "attic"

atticBackground = pygame.image.load("final_project_attic.jpeg")
atticBackground = pygame.transform.scale(atticBackground,(750,500))

def Escape(player):
    
    while player._location == "attic":
        display.blit(atticBackground,(0,0))
        pygame.display.update()
        
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
        
    
    pygame.QUIT
    
Escape()