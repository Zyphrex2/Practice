# KeyEvents02.py
# This program demonstrates that the computer
# can "listen" for multiple different keys.
# It also shows that CAPITAL 'Q' and lowercase 'q'
# are treated as different keys.


from Graphics import *


def displayq():  
   clear()
   setRandomColor()
   drawString("You pressed lowercase q.",100,150,"Arial",28,"bold")
   update()

def displayQ():  
   clear()
   setRandomColor()
   drawString("You pressed CAPITAL Q.",100,150,"Arial",28,"bold")
   update()



##########
#  MAIN  #
##########


beginGrfx(800,500)
listen()
onkey(displayq,"q")
onkey(displayQ,"Q")
endGrfx()
   