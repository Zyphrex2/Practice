# KeyEvents06.py
# This program demonstrates that the string literal 
# "key symbols" used for the "Special Keys" are 
# "Case-Sensitive". 


from Graphics import *


def moveUp():  
   global y
   y -= 10
   clear()
   fillCircle(x,y,r)
   update()  

def moveDown():  
   global y
   y += 10
   clear()
   fillCircle(x,y,r)
   update()  
   
def moveLeft():  
   global x
   x -= 10
   clear()
   fillCircle(x,y,r)
   update()  

def moveRight():  
   global x
   x += 10
   clear()
   fillCircle(x,y,r)
   update()   

def bigger():  
   global r
   r += 10
   clear()
   fillCircle(x,y,r)
   update()   
   
def smaller():  
   global r
   r -= 10
   if r < 0:
      r = 0
   clear()
   fillCircle(x,y,r)
   update()     

def center():  
   global x,y,r
   x = 400
   y = 250
   r = 50
   clear()
   fillCircle(x,y,r)
   update()  
   
   
   
##########
#  MAIN  #
##########


x = 400
y = 250
r = 50

beginGrfx(800,500)
listen()
onkeypress(moveUp,"up")  # should be "Up"
onkeypress(moveDown,"Down")
onkeypress(moveLeft,"Left")
onkeypress(moveRight,"Right")
onkeypress(bigger,"Insert")
onkeypress(smaller,"Delete")
onkey(center,"Home")
fillCircle(x,y,r)
endGrfx()
   