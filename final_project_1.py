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
BLACK = (0,0,0)
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
        text = ""
        for i in range(len(list2)):
            textSurface1 = pygame.font.Font(None,32).render(list1[i],True,BLACK)
            display.blit(textSurface1,(160,55))
            while text != list2[i]:
                for event in pygame.event.get():
                    if event == pygame.K_BACKSPACE:
                        text = text[:-1] 
                    elif event.type == pygame.KEYDOWN:
                        text += event.unicode
                        
                textSurface2 = pygame.font.Font(None,32).render(text,True,BLACK)
                display.blit(textSurface2,(200,55))

    


atticBackground = pygame.image.load("attic.jpeg")
atticBackground = pygame.transform.scale(atticBackground,(750,400))


couch = pygame.image.load("couch.png")
couch = pygame.transform.scale(couch,(150,75))
couch = Sprite(couch,200,245)

couchBground = pygame.image.load("couch.png")
couchBground = pygame.transform.scale(couchBground,(750,400))

blank = pygame.Surface((450,300))
blank.fill(WHITE)

inversionQuestions = [
    'Traduisez “Will you(informal) escape this room?” utilizer inversion.'
    'Changer “Est-ce que nous aimons les examens” à inversion.'
    'Changer “Est-ce que elle est contente?” à inversion.']

inversionAnswers = [
    'Echapperas-tu cette chambre?'
    'Aimons-nous les examens?'
    'Est-t-elle contente?']


def Escape(player):
    
    player = Player()
    
    
    
    while player._location == "attic":
       goto(atticBackground)
       display.blit(couch.image,(200,245))
       click(player,couch, "couch")
       
       pygame.display.update() 
       
    while player._location == "couch":
        goto(couchBground)
        display.blit(blank,(150,50)) 
        answer(inversionQuestions,inversionAnswers)
        pygame.display.update()       
                    
        
    
    pygame.QUIT
  
x = "player"
Escape(x)