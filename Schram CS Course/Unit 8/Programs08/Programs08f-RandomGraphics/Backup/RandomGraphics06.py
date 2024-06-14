# RandomGraphics06.py
# This program displays 500 randomly colored squares.  
# Creating the random colors is also simplified 
# with the <setRandomColor> procedure.


from Graphics import *
from random import randint

beginGrfx(1300,700)

for k in range(500):
   x = randint(0,1300)
   y = randint(0,700)
   radius = randint(1,150)
   sides = 4
   setRandomColor()
   fillRegularPolygon(x,y,radius,sides)
 
endGrfx()
