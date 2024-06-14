# RandomGraphics07.py
# This program displays 500 randomly colored 
# polygons with a random number of sides.


from Graphics import *
from random import randint

beginGrfx(1300,700)

for k in range(500):
   x = randint(0,1300)
   y = randint(0,700)
   radius = randint(1,150)
   sides = randint(3,10)
   setRandomColor()
   fillRegularPolygon(x,y,radius,sides)
 
endGrfx()
