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

class Player: #class to give player attribute
    def __init__(self):
        self._location = "room3" #determines what room player is in
        
class Sprite(pygame.sprite.Sprite): #class to create Sprites
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect.move(self.rect,x,y)
        
        
        
def goto(room):
    display.blit(room,(0,0))
    
    
def click(player,x,y): #if mouse clicks a sprite (x) sends player location to y
        ev = pygame.event.get()
        for event in ev:
                if event.type == pygame.MOUSEBUTTONDOWN:
                   pos = pygame.mouse.get_pos()
                   if pygame.Rect.collidepoint(x.rect, pos):
                        print("this works")
                        player._location = y


    

def answer(player,list1,list2,room): #allows player to type answers and moves on when they're correct
        
        Qplacement = [55,115,175,235]
        Aplacement = [100,160,220,280]
    
        for i in range(len(list2)):
            text = ""
            
            accent1 = pygame.font.Font(None,32).render("é",True,BLACK)
            accent2 = pygame.font.Font(None,32).render("ê",True,BLACK)
            accent3 = pygame.font.Font(None,32).render("à",True,BLACK)
            accent4 = pygame.font.Font(None,32).render("è",True,BLACK)
            
            display.blit(blank2,(0,400))
            display.blit(accent1,(10,410))
            display.blit(accent2,(30,410))
            display.blit(accent3,(50,410))
            display.blit(accent4,(10,450))
            
            pygame.display.update()
            
            accent1rect = pygame.Rect(10,410,20,32)
            accent2rect = pygame.Rect(30,410,20,32)
            accent3rect = pygame.Rect(50,410,20,32)
            accent4rect = pygame.Rect(10,450,20,32)
            
            textSurface1 = pygame.font.Font(None,16).render(list1[i],True,BLACK)
            display.blit(textSurface1,(160,Qplacement[i]))
            pygame.display.update()
            while text != list2[i]:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pygame.Rect.collidepoint(accent1rect, pos):
                            text += "é"
                        elif pygame.Rect.collidepoint(accent2rect, pos):
                            text += "ê"
                        elif pygame.Rect.collidepoint(accent3rect, pos):
                            text += "à"
                        elif pygame.Rect.collidepoint(accent4rect, pos):
                            text += "è"
                    elif event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                            display.blit(delete,(150,Aplacement[i]))
                            text = text[:-1]
                        elif event.type == pygame.KEYDOWN:
                            text += event.unicode
                       
                    textSurface2 = pygame.font.Font(None,16).render(text,True,BLACK)
                    display.blit(delete,(150,Aplacement[i]))
                    display.blit(textSurface2,(160,Aplacement[i]))
                    pygame.display.update()
        player._location = room
        
       

    


atticBackground = pygame.image.load("attic.jpeg")
atticBackground = pygame.transform.scale(atticBackground,(750,400))

roombackground1 = pygame.image.load("final_project_room2.jpeg")
roombackground1 = pygame.transform.scale(roombackground1, (750,400))

roombackground2 = pygame.image.load("final_project_room3.jpeg")
roombackground2 = pygame.transform.scale(roombackground2, (750,400))

roombackground3 = pygame.image.load("room5.png")
roombackground3 = pygame.transform.scale(roombackground3, (750,400))

roombackground4 = pygame.image.load("room6.jpeg")
roombackground4 = pygame.transform.scale(roombackground4,(750,400))

couchBground = pygame.image.load("couch.png")
couchBground = pygame.transform.scale(couchBground,(750,400))

escaped = pygame.image.load("escaped.jpeg")
escaped = pygame.transform.scale(escaped,(750,500))

bar1 = pygame.image.load("progressbar1.png")
bar1 = pygame.transform.scale(bar1,(300,50))

bar2 = pygame.image.load("progressbar2.png")
bar2 = pygame.transform.scale(bar2,(300,50))

bar3 = pygame.image.load("progressbar3.png")
bar3 = pygame.transform.scale(bar3,(300,50))

couch = pygame.image.load("couch.png")
couch = pygame.transform.scale(couch,(150,75))
couch = Sprite(couch,200,245)

lock = pygame.image.load("lock.png")
lock = pygame.transform.scale(lock,(15,20))
lock10 = Sprite(lock,500,300)
lock11 = Sprite(lock,100,100)

lock2 = pygame.image.load("openkey.png")
lock2 = pygame.transform.scale(lock2,(15,20))
lock20 = Sprite(lock2,500,300)
lock21 = Sprite(lock2,100,100)

chair = pygame.image.load("purplechair.png")
chair = pygame.transform.scale(chair,(150,175))
chair = Sprite(chair,400,225)

chair2 = pygame.image.load("chair2.png")
chair2 = pygame.transform.scale(chair2,(150,175))
chair2 = Sprite(chair2,400,225)

couch2 = pygame.image.load("couch2.png")
couch2 = pygame.transform.scale(couch2,(275,125))
couch2 = Sprite(couch2,10,245)

lamp = pygame.image.load("lamp.png")
lamp = pygame.transform.scale(lamp,(100,150))
lamp = Sprite(lamp,600,175)

lamp2 = pygame.image.load("lamp2.png")
lamp2 = pygame.transform.scale(lamp2,(100,150))
lamp2 = Sprite(lamp2,100,225)

blank = pygame.Surface((450,300))
blank.fill(WHITE)
blank2 = pygame.Surface((750,100))
blank2.fill(WHITE)

delete = pygame.Surface((450,20))
delete.fill(WHITE)




inversionQuestions = [
    'Traduisez “Will you(informal) escape this room?” utilizer inversion.',
    'Changer “Est-ce que nous aimons les examens” à inversion.',
    'Changer “Est-ce que tu es contente?” à inversion.']

passeQuestions = [
    'Traduisez à Français, “We went to the party yesterday.”',
    'Traduisez à Francais, “You all saw the dogs at the park”']
imparfaitQuestions = [   
    'Traduizes “I was a good singer.” (masculin)',
    'Traduizes “I was doing my homework when you all arrived.”']
reflexiveQuestions = [    
    'Traduizes “I comb my hair and I comb her hair.”',
    'Traduizes “I miss you.”',
    'Traduizes “If it pleases you.”']
negationQuestions = [
    'Traduizes “We hardly go to the movies.”',
    'Traduizes “I no longer love you.”',
    'Traduizes “I only have the blue one”',
    'Traduizes “Nobody likes me.”']


inversionAnswers = [
    'Echapperas-tu cette chambre?',
    'Aimons-nous les examens?',
    'Es-tu contente?']
passeAnswers = [    
    'Nous sommes allés à la fête hier',
    "Vous avez vu les chiens au parc"]
imparfaitAnswers = [   
   
    "J'étais un bon chanteur",
    "Je faisais mes devoirs quand vous êtes arrivés"]
reflexiveAnswers = [    
    'Je me peigne les cheveux et je peigne ses cheveux',
    'Tu me manque',
    "S'il te plait"]
negationAnswers = [
    "Nous n’allons guère au cinèma",
    "Je ne t’aime plus",
    "Je n'ai que le bleu",
    "Personne ne m’aime"]


def Escape(player): #main function
    
    player = Player()
    
    a = True
    while a == True:
        while player._location == "attic":
           goto(atticBackground)
           display.blit(couch.image,(200,245))
           
           click(player,couch, "couch")
           
           
           pygame.display.update() 
           
        while player._location == "couch":
            goto(couchBground)
            display.blit(blank,(150,50)) 
            answer(player,inversionQuestions,inversionAnswers,'room1')
            
            pygame.display.update()   
       
        while player._location == "room1":
            goto(roombackground1)
            display.blit(lamp.image,(600,175))
            click(player,lamp,"lamp")
           
            pygame.display.update()
            
        while player._location == "lamp":
            goto(roombackground1)
            display.blit(blank,(150,50))
            answer(player,passeQuestions,passeAnswers,"room2")
            pygame.display.update()
        
        while player._location == "room2":
            goto(roombackground3)
            display.blit(chair.image,(400,225))
            click(player,chair,"chair")
            pygame.display.update()
        
            
               
        while player._location == "chair":
             goto(roombackground3)
             display.blit(blank,(150,50))
             answer(player,imparfaitQuestions,imparfaitAnswers,"room3")
         
        while player._location == "room3":
            goto(roombackground2)
            display.blit(couch2.image,(10,245))
            click(player,couch2,"couch2")
            
            
            pygame.display.update()
            
        while player._location == "couch2":
            goto(roombackground2)
            display.blit(blank,(150,50))
            answer(player,negationQuestions,negationAnswers,"room4")
            
            pygame.display.update()
            
        while player._location == "room4":
            goto(roombackground4)
            display.blit(chair2.image,(400,225))
            click(player,chair2,"chair2")
            
            pygame.display.update()
            
        while player._location == "chair2":
            goto(roombackground4)
            display.blit(blank,(150,50))
            answer(player,reflexiveQuestions,reflexiveAnswers,"finished")
            
            pygame.display.update
            
        while player._location == "finished":
            goto(escaped)
            ev = pygame.event.get()
            for event in ev:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    a = False
            
            pygame.display.update()
       
    pygame.QUIT
  
x = "player"
Escape(x)