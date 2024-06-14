# RandomGraphics03.py
# This program displays 1000 random lines.


from Graphics import *
from random import randint

beginGrfx(1300,700)

for k in range(1000):
   x1 = randint(0,1300)
   y1 = randint(0,700)
   x2 = randint(0,1300)
   y2 = randint(0,700)
   drawLine(x1,y1,x2,y2)

endGrfx()
