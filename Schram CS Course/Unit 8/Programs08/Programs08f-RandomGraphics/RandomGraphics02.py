# RandomGraphics02.py
# This program displays a circle in a fixed location 
# with a fixed size.  3 random values are generated. 
# Two are used for the center location of the circle 
# and a third is used for its radius.


from Graphics import *
from random import randint

beginGrfx(1300,700)

drawCircle(650,350,250)

setColor("red")
x = randint(150,1150)
y = randint(150,550)
r = randint(10,150)
drawCircle(x,y,r)

endGrfx()
