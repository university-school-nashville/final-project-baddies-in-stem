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
        
def goto(room):
    display.blit(room,(0,0))
    
    
def click(self,x,y):
    ev = pygame.event.get()
    for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
               pos = pygame.mouse.get_pos()
               if pygame.x.collide_rect(x,pos):
                    goto(x)
                    self._activity = y
    
                    
    
    

atticBackground = pygame.image.load("attic.jpeg")
atticBackground = pygame.transform.scale(atticBackground,(750,400))

couch = pygame.image.load("couch.png")
couch = pygame.transform.scale(couch,(200,100))


def Escape(player):
    
    player = Player()
    
    goto(atticBackground)
    display.blit(couch,(200,225))
    pygame.display.update()
    
    while player._location == "attic":
       
        click(player,couch,"couch")
    
        
       
                    
        
    
    pygame.QUIT
  
x = "player"
Escape(x)