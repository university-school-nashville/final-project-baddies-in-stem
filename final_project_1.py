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
        self._progress = 0
        
class Sprite(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect.move(self.rect,x,y)
        
        
        
def goto(room):
    display.blit(room,(0,0))
    
    
def click(player,x,y):
    ev = pygame.event.get()
    for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN:
               pos = pygame.mouse.get_pos()
               if pygame.Rect.collidepoint(x.rect, pos):
                    print("this works")
                    player._location = y

def answer(list1,list2):
    for i in range[list1]:
        answer = ""
        for event in pygame.event.get():
            if event.key == pygame.K_BACKSPACE:
                answer = answer[:-1]
            elif event.key == pygame.K_RETURN and answer == list2[i]:
                i += 1
            else:
                answer += event.unicode
    

atticBackground = pygame.image.load("attic.jpeg")
atticBackground = pygame.transform.scale(atticBackground,(750,400))


couch = pygame.image.load("couch.png")
couch = pygame.transform.scale(couch,(150,75))
couch = Sprite(couch,200,225)

couchBground = pygame.image.load("couch.png")
couchBground = pygame.transform.scale(couchBground,(750,400))



def Escape(player):
    
    player = Player()
    
    
    
    while player._location == "attic":
       goto(atticBackground)
       display.blit(couch.image,(200,225))
       click(player,couch, "couch")
       
       pygame.display.update() 
       
    while player._location == "couch":
        goto(couchBground)
               
        pygame.display.update()       
                    
        
    
    pygame.QUIT
  
x = "player"
Escape(x)