# Animation14.py
# This program animates a snowman across the screen 
# by placing 3 circles in the same <for> loop.  
# Note how the "slowing down" problem returns.


from Graphics import *


beginGrfx(1300,700)

setBackground("black")

for x in range(50,1251,1):
   setColor("white")
   fillCircle(x,315,15)
   fillCircle(x,350,25)
   fillCircle(x,405,40)
   delay(10)
   setColor("black")
   fillCircle(x,315,17)
   fillCircle(x,350,27)
   fillCircle(x,405,42)

endGrfx()