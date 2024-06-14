# KeyEvents01.py
# This program introduces "Key Interactivity" 
# by displaying a randomly colored message 
# anytime lowercase 'q' is typed.
# NOTE: This not the same as "Keyboard Input".
# ALSO: The <listen> command is necessary for 
# the <onkey> command to function properly.


from Graphics import *


def displayq():  
   clear()
   setRandomColor()
   drawString("You pressed lowercase q.",100,150,"Arial",28,"bold")
   update()



##########
#  MAIN  #
##########


beginGrfx(800,500)
listen()
onkey(displayq,"q")
endGrfx()
   