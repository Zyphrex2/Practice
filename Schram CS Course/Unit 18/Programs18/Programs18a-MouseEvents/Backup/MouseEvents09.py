# MouseEvents09.py
# This program draws a small red square when
# the mouse is left-clicked and a blue line
# when the mouse in right-clicked.


from Graphics import *


def displayDot(x,y):
   setColor("red")   
   x,y = traditionalXY(x,y)
   fillRectangle(x-7,y-7,x+7,y+7)
   update()
   
def displayLine(x,y): 
   setColor("blue")   
   goto(x,y)  
   update()   



##########
#  MAIN  #
##########

beginGrfx(1300,700)
onscreenclick(displayDot,btn=1)
onscreenclick(displayLine,btn=3)
endGrfx()
   