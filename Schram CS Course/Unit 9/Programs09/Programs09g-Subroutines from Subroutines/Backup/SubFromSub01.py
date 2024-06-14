# SubFromSub01.py
# This program demonstrates a <picket> procedure
# that will be used to help draw a fence.



from Graphics import *


def drawPicket(x):
   fillPolygon([x,700,x,500,x+18,450,x+36,500,x+36,700])
   delay(250)  # delay for 1/4 of a second
   

   
##########
#  MAIN  #
##########

beginGrfx(1200,700)

setBackground("black")
setColor("burlywood")
fillRectangle(0,510,1200,535)
fillRectangle(0,640,1200,665)

setColor("brown")
for x in range(2,1200,40):
   drawPicket(x)
   
endGrfx()
