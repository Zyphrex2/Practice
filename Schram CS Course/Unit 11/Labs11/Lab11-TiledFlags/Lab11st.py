# Lab11st.py
# "Tiled Flags"
# This is the student, starting version, of Lab 11.


from Graphics import *
from time import sleep


tileSpacing = 25      
tileSize = tileSpacing-3  


def drawTile(x,y):
   fillRect(x+2,y+2,tileSize,tileSize)
   setColor("white")
   drawLine(x+2,y+2,x+tileSize,y+2)
   drawLine(x+tileSize,y+2,x+tileSize,y+tileSize)


def showName(name):
   x = len(name)*24
   color("black")
   fillRectangle(1120-x,50,1150,101)
   color("white")
   fillRectangle(1125-x,55,1145,96)   
   color("black")
   drawString(name,1135-x,98,"Courier New",24,"bold") 
   delay(1000) # 1 second delay between flags
   reset()
   tracer(0,0)
   hideturtle()   
     
     
def titlePage(name, period):
   setBackground("gold")
   setColor("white")
   fillRectangle(100,100,1100,550)
   setColor("red")
   drawString("Lab 11, Tiled Flags",175,240,"Arial",54,"bold")
   setColor("blue")
   drawString("by: "+name,175,370,"Arial",54,"bold")
   setColor("green")
   drawString("Period: "+period,175,500,"Arial",54,"bold")
   delay(2000) # Wait 2 seconds before showing first flag.

        
def flagOfLibya():
   setBackground("black")
   for x in range(0,1200,tileSpacing):
      for y in range(0,650,tileSpacing):
         setColor("green")   
         drawTile(x,y)
      update()         
   showName("Libya (1977-2011)")      
      
      
def flagOfPoland():
   setBackground("black")
   for x in range(0,1200,tileSpacing):
      for y in range(0,650,tileSpacing):
         if y < 325:          # top stripe
            setColor("white")
         else:				    	# bottom stripe
            setColor("red")
         drawTile(x,y)
      update()         
   showName("Poland")
      

def flagOfItaly():
   setBackground("black")
   for x in range(0,1200,tileSpacing):
      for y in range(0,650,tileSpacing):
         if x < 400:               # left stripe
            setColor("green")
         if x >= 400 and x < 800:  # middle stripe
            setColor("white")
         if x >= 800:              # right stripe
            setColor("red")         
         drawTile(x,y)
      update()         
   showName("Italy")



def flagOfFrance():
   setBackground("black")
   for x in range(0,1200,tileSpacing):
      for y in range(0,650,tileSpacing):
         if x < 400:               # left stripe
            setColor("Blue")
         if x >= 400 and x < 800:  # middle stripe
            setColor("white")
         if x >= 800:              # right stripe
            setColor("red")         
         drawTile(x,y)
      update()         
   showName("France")


def flagOfIreland():
   setBackground("black")
   for x in range(0,1200,tileSpacing):
      for y in range(0,650,tileSpacing):
         if x < 400:               # left stripe
            setColor("green")
         if x >= 400 and x < 800:  # middle stripe
            setColor("white")
         if x >= 800:              # right stripe
            setColor("orange")         
         drawTile(x,y)
      update()         
   showName("Ireland")


def flagOfRomania():
   setBackground("black")
   for x in range(0,1200,tileSpacing):
      for y in range(0,650,tileSpacing):
         if x < 400:               # left stripe
            setColor("blue")
         if x >= 400 and x < 800:  # middle stripe
            setColor("yellow")
         if x >= 800:              # right stripe
            setColor("red")         
         drawTile(x,y)
      update()         
   showName("Romania")


def flagOfHolland():
   setBackground("black")
   for x in range(0,1200,tileSpacing):
      for y in range(0,650,tileSpacing):
         if y < 217:               # left stripe
            setColor("red")
         if y >= 217 and y < 425:  # middle stripe
            setColor("white")
         if y >= 425:              # right stripe
            setColor("blue")         
         drawTile(x,y)
      update()         
   showName("Holland")


def flagOfHungary():
   setBackground("black")
   for x in range(0,1200,tileSpacing):
      for y in range(0,650,tileSpacing):
         if y < 217:               # left stripe
            setColor("darkRed")
         if y >= 217 and y < 425:  # middle stripe
            setColor("white")
         if y >= 425:              # right stripe
            setColor("darkGreen")         
         drawTile(x,y)
      update()         
   showName("Hungary")


def flagOfGermany():
   setBackground("black")
   for x in range(0,1200,tileSpacing):
      for y in range(0,650,tileSpacing):
         if y < 217:               # left stripe
            setColor("black")
         if y >= 217 and y < 425:  # middle stripe
            setColor("red")
         if y >= 425:              # right stripe
            setColor("yellow")         
         drawTile(x,y)
      update()         
   showName("Germany")


def flagOfSweden():
   setBackground("black")
   for x in range(0,1200,tileSpacing):
      for y in range(0,650,tileSpacing):
         if y > 270 and y < 375 or x > 295 and x < 400:
            setColor("yellow")
         else:
            setColor("blue")   
         drawTile(x,y)
      update()         
   showName("Sweden") 
   

   
                        
##########
#  MAIN  #
##########

beginGrfx(1200,650)

titlePage("David Bardan","5")

#Examples:
flagOfLibya()
flagOfPoland()
flagOfItaly()

#Vertical Stripes:
flagOfFrance()
flagOfIreland()
flagOfRomania()

#Horizontal Stripes:
flagOfHolland()
flagOfHungary()
flagOfGermany()

#Sweden
flagOfSweden()

exit()