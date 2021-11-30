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

def answer(player,list1,list2,list3,list4,room):
        
        for i in range(len(list2)):
            text = ""
            
            textSurface1 = pygame.font.Font(None,16).render(list1[i],True,BLACK)
            display.blit(textSurface1,(160,list3[i]))
            pygame.display.update()
            while text != list2[i]:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                            display.blit(delete,(150,list4[i]))
                            text = text[:-1]
                        elif event.type == pygame.KEYDOWN:
                            text += event.unicode
                       
                    textSurface2 = pygame.font.Font(None,16).render(text,True,BLACK)
                    display.blit(delete,(150,list4[i]))
                    display.blit(textSurface2,(160,list4[i]))
                    pygame.display.update()
        player._location = "attic"
        player._progress = 1

    


atticBackground = pygame.image.load("attic.jpeg")
atticBackground = pygame.transform.scale(atticBackground,(750,400))

roombackground1 = pygame.image.load("final_project_room2.jpeg")
roombackground1 = pygame.transform.scale(roombackground1, (750,400))

roombackground2 = pygame.image.load("final_project_room3.jpeg")
roombackground2 = pygame.transform.scale(roombackground2, (750,400))

roombackground3 = pygame.image.load("room5.png")
roombackground3 = pygame.transform.scale(roombackground3, (750,400))


couch = pygame.image.load("couch.png")
couch = pygame.transform.scale(couch,(150,75))
couch = Sprite(couch,200,245)

lock = pygame.image.load("lock.png")
lock = pygame.transform.scale(lock,(15,20))
lock = Sprite(lock,500,300)

lock2 = pygame.image.load("openkey.png")
lock2 = pygame.transform.scale(lock2,(15,20))
lock2 = Sprite(lock2,500,300)

couchBground = pygame.image.load("couch.png")
couchBground = pygame.transform.scale(couchBground,(750,400))

chair = pygame.image.load("purplechair.png")
chair = pygame.transform.scale(chair,(15,20))
chair = Sprite(chair,200,245)

bed = pygame.image.load("final_project_bed2.png")
bed = pygame.transform.scale(bed,(15,20))
bed = Sprite(bed,200,245)

lamp = pygame.image.load("lamp.png")
lamp = pygame.transform.scale(lamp,(15,20))
lamp = Sprite(lamp,200,245)



blank = pygame.Surface((450,300))
blank.fill(WHITE)

delete = pygame.Surface((450,20))
delete.fill(WHITE)


Qplacement = [55,115,175,235]
Aplacement = [100,160,220,280]

inversionQuestions = [
    'Traduisez “Will you(informal) escape this room?” utilizer inversion.',
    'Changer “Est-ce que nous aimons les examens” à inversion.',
    'Changer “Est-ce que elle est contente?” à inversion.']

passeQuestions = [
    'Traduisez à Français, “We went to a party yesterday.”',
    'Traduisez à Anglais, “Vous êtes vus les chiens au parc.”']
imparfaitQuestions = [   
    'Traduizes “I was a good singer.” utilizer l’inversion',
    'Traduizes “I was doing my homework when you all arrived.”']
reflexiveQuestions = [    
    'Traduizes “I comb my hair and I comb her hair.”',
    'Traduizes “I miss you.”',
    'Traduizes “If it pleases you.”']
negationQuestions = [
    'Traduizes “We hardly go to the movies.”',
    'Traduizes “I no longer love you.”',
    'Traduizes “I only went because you all told me to go.”',
    'Traduizes “Nobody likes me.”']


inversionAnswers = [
    'Echapperas-tu cette chambre?',
    'Aimons-nous les examens?',
    'Est-t-elle contente?']
passeAnswers = [    
    'Nous sommes allés à la fête hier.',
    'You all saw the dogs at the park.']
imparfaitAnswers = [   
    'J’était un bon chanteur.',
    'Je faisais mon devoirs quand vous etes arrivés.']
reflexiveAnswers = [    
    'Je me peigne les cheveux et je peigne ses cheveux.',
    'Tu me manque.',
    'Si te plait.']
negationAnswers = [
    'Nous n’allons guère au cinèma.',
    'Je ne t’aime plus.',
    'Je ne suis que allé parce que vous m’avez dit aller.',
    'Personne ne m’aime.']


def Escape(player):
    
    player = Player()
    
    
    while True:
        while player._location == "attic":
           goto(atticBackground)
           display.blit(couch.image,(200,245))
           if player._progress == 0:
               display.blit(lock.image(500,300))
               click(player,lock,"lock")
           if player._progress ==1:
               display.blit(lock2.image(500,300))
               click(player,lock2,"lock")
           click(player,couch, "couch")
           
           
           pygame.display.update() 
           
        while player._location == "couch":
            goto(couchBground)
            display.blit(blank,(150,50)) 
            answer(player,inversionQuestions,inversionAnswers,Qplacement,Aplacement,atticBackground)
            
            pygame.display.update()   
            
        while player._location == "lock":
            if player._progress == 0:
                player._location = "attic"
            if player._progress == 1:
                player._location = "room"
                player._progress = 0
            
        
    
       
       
       
                    
        
    
    pygame.QUIT
  
x = "player"
Escape(x)