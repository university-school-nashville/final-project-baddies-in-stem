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
        self._activity = "none"
        
def goto(room,thing):
    display.blit(room,(0,0))
    display.blit(thing,(10,300))

atticBackground = pygame.image.load("attic.jpeg")
atticBackground = pygame.transform.scale(atticBackground,(750,400))

couch = pygame.image.load("couch.jpg")
couch = pygame.transform.scale(couch,(200,100))


def Escape(player):
    
    player = Player()
    
    goto(atticBackground,couch)
    pygame.display.update()
    
    while player._location == "attic":
       
    
        
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
               # pos = pygame.mouse.get_pos()
               # if 10 <= pos[0] and pos[0]<=300  and 300 >= pos[1] and pos[1] >= 200:
                    goto(couch)
                    
        
    
    pygame.QUIT
  
x = "player"
Escape(x)