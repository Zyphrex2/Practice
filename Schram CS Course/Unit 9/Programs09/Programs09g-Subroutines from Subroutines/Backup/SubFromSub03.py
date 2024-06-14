# SubFromSub03.py
# This program adds procedure <drawNightSky>, 
# which is created using procedures <drawMoon> 
# and <drawRandomStar>.



from Graphics import *
from random import randint


def drawPicket(x):
   fillPolygon([x,700,x,500,x+18,450,x+36,500,x+36,700])
   delay(250)  # delay for 1/4 of a second
   
   
def drawFence():
   # cross beams
   setColor("burlywood")
   fillRectangle(0,510,1200,535)
   fillRectangle(0,640,1200,665)
   # pickets
   setColor("brown")
   for x in range(2,1200,40):
      drawPicket(x)   


def drawMoon():
   setColor("white")
   fillCircle(1110,95,70)
   setColor("black")
   fillCircle(1075,80,60)  
   
   
def drawRandomStar(x):
   y = randint(40,200)
   radius = randint(15,25)
   points = randint(5,10)
   fillStar(x,y,radius,points)
   delay(250)


def drawNightSky(): 
   setBackground("black")
   drawMoon()
   setColor("white")
   for x in range(40,1001,60):
      drawRandomStar(x)
      
      
      
##########
#  MAIN  #
##########

beginGrfx(1200,700)

drawNightSky()
drawFence()
   
endGrfx()
