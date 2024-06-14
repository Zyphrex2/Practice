# MouseEvents03.py
# This program demonstrates that the <x> and <y>
# parameters store the location where the user
# clicked on the screen.  The problem is, the
# coordinate displayed is based on "Turtle Graphics"
# where (0,0) is in the center of the screen.
# This results in some negative coordinates.


from Graphics import *


def display(x,y):
   clear()
   drawString("Mouse clicked at ("+str(x)+","+str(y)+")",100,150,"Arial",28,"normal")



##########
#  MAIN  #
##########

beginGrfx(1300,700)
onscreenclick(display)
endGrfx()
   