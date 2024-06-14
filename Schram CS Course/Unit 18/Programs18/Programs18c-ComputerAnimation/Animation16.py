# Animation16.py
# This program shows another major problem with 
# "Draw-And-Erase Animation."  It falls flat on 
# its face when you have a multi-colored background.


from Graphics import *


def drawColorfulBackground():
   for c in range(10):
      setColor(c+1)
      fillRectangle(c*130, 0, (c+1)*130, 700)
      
      

##########
#  MAIN  #
##########
      
beginGrfx(1300,700)

drawColorfulBackground()

for x in range(50,1251,2):
   setColor("white")
   fillCircle(x,315,15)
   fillCircle(x,350,25)
   fillCircle(x,405,40)
   delay(10)
   setColor("red")
   fillCircle(x,315,17)
   fillCircle(x,350,27)
   fillCircle(x,405,42)

endGrfx()
