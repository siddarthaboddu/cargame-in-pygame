import pygame
from pygame import *
import time
import random

pygame.init()
width=800
length=600
gamedisp=pygame.display.set_mode((width,length))
pygame.display.set_caption("wwwooww")
clock=pygame.time.Clock()

blue=(255,255,255)
black=(0,0,0)
green=(0,255,0)
myimg=pygame.image.load("car.png").convert_alpha()
x=width/2
y=length-180
score=0
x_change=0
y_change=0
o_w=100
o_x=random.randrange(0,width-o_w)

o_h=100
o_y=0
speed=20 #random.randrange(3,6,1)

def car(x,y):
    gamedisp.blit(myimg,(x,y))

def objects(o_x,o_y,o_w,o_h,color):
    global score
    pygame.draw.rect(gamedisp,green,(o_x,o_y,o_w,o_h))
    
def object_crash():
    global x,y,o_x,o_y,green,o_h,o_w,score
    if(y+10<o_y+100 and y+10>o_y and x<o_x+100 and x>o_x ):
        print("1")
        score=0
        
        crash()
    if(y+144<o_y+100 and y+144>o_y and x<o_x+100 and x>o_x ):
        print("2")
        score=0
        
        crash()
    if(y+5<o_y+100 and y+5>o_y and x+60<o_x+100 and x+60>o_x ):
        print("3")
        score=0
        
        crash()    
    if(y+144<o_y+100 and y+144>o_y and x+64<o_x+100 and x+64>o_x ):
        print("4")
        score=0
        car(x,y)
        pygame.display.update()
        crash()    
    if(y+10<o_y+100 and x<o_x and x+64>x+100):
        print("5")
        score=0
        crash()
def new_object():
    global o_x,o_y,green,o_h,o_w,score,speed
    if(o_y>600+147):
        o_y=0
        o_x=random.randrange(0,800-o_w)
        score+=1
        speed=speed+5
        objects(o_x,o_y,o_w,o_h,green)
        
def boundary(a,b):
    if(a>width-64):
        a=width-64
        crash()
    if(a<0):
        a=0
        crash()
    if(b>length-144):
        b=length-144
        crash()
    if(b<0):
        b=0
        crash()
    return (a,b)

def crash():
    display_text('you crashed dude')

def display_text(text):
    fonttext=pygame.font.Font('freesansbold.ttf',50)
    textdisp=fonttext.render(text, True, black)
    position=textdisp.get_rect()
    position.center=(400,300)
    gamedisp.blit(textdisp,position)
    pygame.display.update()
    time.sleep(1)
    game()
    
def intro():
    introdisp=[1,2,3]
    introposition=[1,2,3]
    myintro=pygame.image.load("intro.jpg").convert_alpha()
    gamedisp.blit(myintro,(0,0))
    logo=pygame.image.load("logo.png").convert_alpha()
    gamedisp.blit(logo,(200,25))

    '''introfont=pygame.font.Font('freesansbold.ttf',100)'''
    enter_quitfont=pygame.font.Font('freesansbold.ttf',25)
    #introdisp[0]=introfont.render("car race ",True,(0,0,0))
    introdisp[1]=enter_quitfont.render("*enter ",True,(255,255,255))
    introdisp[2]=enter_quitfont.render("*quit ",True,(255,255,255))
    #introposition[0]=introdisp[0].get_rect()
    introposition[1]=introdisp[1].get_rect()
    introposition[2]=introdisp[2].get_rect()
    #introposition[0].center=(300,50)
    introposition[1].center=(750,400)
    introposition[2].center=(750,450)
    
    #gamedisp.blit(introdisp[0],introposition[0])
    gamedisp.blit(introdisp[1],introposition[1])
    gamedisp.blit(introdisp[2],introposition[2])
    pygame.display.update()
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    game()
                 


    
def game():
    global x,y,x_change,y_change,o_w,o_h,o_x,o_y,speed
    end=False
    while not end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-20
                    o_y=o_y+speed
                if event.key==pygame.K_RIGHT:
                    x_change=+20
                    o_y=o_y+speed
               
               
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    x_change=0
                if event.key==pygame.K_RIGHT:
                    x_change=0
            
              
            #car change
            x=x+x_change
            y=y+y_change
            #object_crash
            object_crash()
            
            
            #new object
            new_object()
            
            #boundary
            (x,y)=boundary(x,y)
        gamedisp.fill(blue)
        #score
        fonttext=pygame.font.Font('freesansbold.ttf',15)
        scoretext=fonttext.render("score:"+str(score),True,black)
       
        gamedisp.blit(scoretext,(0,0))
        #def objects(o_x,o_y,o_w,o_h,color):
        objects(o_x,o_y,o_w,o_h,green)
        
        #car
        car(x,y)
        
        
        pygame.display.update()
        
        clock.tick(30)

intro()
pygame.quit()
quit()
