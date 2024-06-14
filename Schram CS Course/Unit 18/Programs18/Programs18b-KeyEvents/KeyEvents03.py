# KeyEvents03.py
# This program controls the movement of a
# circle on the screen using the letters:
#    w
#   a s
#    z


from Graphics import *


def moveUp():  
   global y
   y -= 10
   clear()
   fillCircle(x,y,50)
   update()  

def moveDown():  
   global y
   y += 10
   clear()
   fillCircle(x,y,50)
   update()  
   
def moveLeft():  
   global x
   x -= 10
   clear()
   fillCircle(x,y,50)
   update()  

def moveRight():  
   global x
   x += 10
   clear()
   fillCircle(x,y,50)
   update()   



##########
#  MAIN  #
##########


x = 400
y = 250

beginGrfx(800,500)
listen()
onkey(moveUp,"w")
onkey(moveDown,"z")
onkey(moveLeft,"a")
onkey(moveRight,"s")
fillCircle(x,y,50)
endGrfx()
   