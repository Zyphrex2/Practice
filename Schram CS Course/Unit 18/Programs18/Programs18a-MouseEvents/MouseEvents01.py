# MouseEvents01.py
# This program introduces "Mouse Interactivity"
# with the <onscreenclick> event which is triggered
# any time the user clicks on the graphics screen
# with the left mouse button.


from Graphics import *


def display(x,y):    # Parameters (x,y) are required 
   global numClicks  # even if they are not used.
   clear()
   numClicks += 1
   drawString("Number of clicks: "+str(numClicks),100,150,"Arial",28,"normal")
   update()



##########
#  MAIN  #
##########

numClicks = 0
beginGrfx(800,500)
onscreenclick(display)
endGrfx()
   