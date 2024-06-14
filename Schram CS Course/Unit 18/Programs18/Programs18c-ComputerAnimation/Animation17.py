# Animation17.py
# This program shows how to handle a multi-colored
# background. By using "Draw-And-Redraw Animation" 
# instead of "Draw-And-Erase" the entire background
# is redrawn every time the object moves.


from Graphics import *


def drawColorfulBackground():
   for c in range(10):
      setColor(c+1)
      fillRectangle(c*130, 0, (c+1)*130, 700)
      
      

##########
#  MAIN  #
##########
      
beginGrfx(1300,700)

for x in range(50,1251,2):
   clear()
   drawColorfulBackground()
   setColor("white")
   fillCircle(x,315,15)
   fillCircle(x,350,25)
   fillCircle(x,405,40)
   delay(10)

endGrfx()
