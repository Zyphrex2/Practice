# MouseEvents07.py
# This program fixes the issue of the previous program
# by using the <traditionalXY> function of the <Graphics> 
# library.  The result is the coordinate is converted to
# "Traditional Graphics" where (0,0) is in the top-left 
# corner and all coordinate values are positive.


from Graphics import *


def display(x,y):
   x,y = traditionalXY(x,y)
   clear()
   drawString("Mouse clicked at ("+str(x)+","+str(y)+")",100,150,"Arial",28,"normal")



##########
#  MAIN  #
##########

beginGrfx(1300,700)
onscreenclick(display)
endGrfx()
   