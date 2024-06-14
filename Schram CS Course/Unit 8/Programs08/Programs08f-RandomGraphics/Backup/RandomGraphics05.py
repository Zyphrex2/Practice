# RandomGraphics05.py
# This program displays 500 randomly colored 
# solid circles with random radii.


from Graphics import *
from random import randint

beginGrfx(1300,700)

for k in range(500):
   x = randint(0,1300)
   y = randint(0,700)
   red = randint(0,255)
   green = randint(0,255)
   blue = randint(0,255)
   radius = randint(1,150)
   setColor(red,green,blue)
   fillCircle(x,y,radius)
 
endGrfx()