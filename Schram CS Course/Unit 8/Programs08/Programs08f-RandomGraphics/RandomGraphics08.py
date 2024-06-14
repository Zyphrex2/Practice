# RandomGraphics08.py
# This program demonstrates that even the
# width of the lines can be random.


from Graphics import *
from random import randint

beginGrfx(1300,700)

for k in range(500):
   x = randint(0,1300)
   y = randint(0,700)
   radius = randint(1,150)
   numLines = randint(3,10)
   setRandomColor()
   w = randint(1,30)
   width(w)
   drawBurst(x,y,radius,numLines)
 
endGrfx()
