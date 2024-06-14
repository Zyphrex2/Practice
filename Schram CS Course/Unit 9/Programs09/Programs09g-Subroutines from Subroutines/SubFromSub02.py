# SubFromSub02.py
# This program uses the <drawPicket> procedure
# to create the <drawFence> procedure.


from Graphics import *


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

   
##########
#  MAIN  #
##########

beginGrfx(1200,700)

setBackground("black")
drawFence()
   
endGrfx()

