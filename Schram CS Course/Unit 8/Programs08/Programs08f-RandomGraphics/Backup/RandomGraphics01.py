# RandomGraphics01.py
# This program first displays two black lines in a
# fixed location.  This is followed by generating 
# four random values, which are used to draw a third, 
# red line in a random location.


from Graphics import *
from random import randint

beginGrfx(1300,700)

drawLine(650,0,650,700)
drawLine(0,350,1300,350)

setColor("red")
x1 = randint(0,1300)
y1 = randint(0,700)
x2 = randint(0,1300)
y2 = randint(0,700)
drawLine(x1,y1,x2,y2)

endGrfx()
