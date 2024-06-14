# MouseEvents02.py
# This program demonstrates how to distinguish between
# the left, middle and right mouse buttons on a Windows PC.
# NOTE: Some mice have a "middle" button; most do not.
# ALSO: On some mice, the "wheel" is clickable and is
#       actually interpreted as the middle button.


from Graphics import *


def leftDisplay(x,y):
   global numLeftClicks
   clear()
   numLeftClicks += 1
   drawString("Number of left clicks: "+str(numLeftClicks),100,150,"Arial",28,"normal")
   drawString("Number of middle clicks: "+str(numMiddleClicks),100,250,"Arial",28,"normal")
   drawString("Number of right clicks: "+str(numRightClicks),100,350,"Arial",28,"normal")


def middleDisplay(x,y):
   global numMiddleClicks
   clear()
   numMiddleClicks += 1
   drawString("Number of left clicks: "+str(numLeftClicks),100,150,"Arial",28,"normal")
   drawString("Number of middle clicks: "+str(numMiddleClicks),100,250,"Arial",28,"normal")
   drawString("Number of right clicks: "+str(numRightClicks),100,350,"Arial",28,"normal")


def rightDisplay(x,y):
   global numRightClicks
   clear()
   numRightClicks += 1
   drawString("Number of left clicks: "+str(numLeftClicks),100,150,"Arial",28,"normal")
   drawString("Number of middle clicks: "+str(numMiddleClicks),100,250,"Arial",28,"normal")
   drawString("Number of right clicks: "+str(numRightClicks),100,350,"Arial",28,"normal")



##########
#  MAIN  #
##########

numLeftClicks = 0
numMiddleClicks = 0
numRightClicks = 0
beginGrfx(800,500)
onscreenclick(leftDisplay,btn=1)
onscreenclick(middleDisplay,btn=2)
onscreenclick(rightDisplay,btn=3)
endGrfx()
   