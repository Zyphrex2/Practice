# MouseEvents03.py
# This program demonstrates how to distinguish between a
# left/1-finger click and a right/2-finger click on a Mac.
# NOTE: On a Mac, button 2 is for right/2-finger click.
# ALSO: There is no middle-click on a Mac.


from Graphics import *


def leftDisplay(x,y):
   global numLeftClicks
   clear()
   numLeftClicks += 1
   drawString("Number of left/1-finger clicks: "+str(numLeftClicks),100,150,"Arial",28,"normal")
   drawString("Number of right/2-finger clicks: "+str(numRightClicks),100,350,"Arial",28,"normal")


def rightDisplay(x,y):
   global numRightClicks
   clear()
   numRightClicks += 1
   drawString("Number of left/1-finger clicks: "+str(numLeftClicks),100,150,"Arial",28,"normal")
   drawString("Number of right/2-finger clicks: "+str(numRightClicks),100,350,"Arial",28,"normal")



##########
#  MAIN  #
##########

numLeftClicks = 0
numRightClicks = 0
beginGrfx(800,500)
onscreenclick(leftDisplay,btn=1)  
onscreenclick(rightDisplay,btn=2)
endGrfx()
   