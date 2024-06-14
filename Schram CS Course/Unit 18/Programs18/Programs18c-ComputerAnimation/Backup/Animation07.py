# Animation07.py
# This program makes the animation as smooth
# as possible by having an increment of just 
# 1 pixel in the <for> loop.
# The delay is also made smaller.


from Graphics import *


beginGrfx(1300,700)

for x in range(50,1251,1):
   setColor("black")
   fillCircle(x,350,25)
   delay(10)
   setColor("white")
   fillCircle(x,350,25)

endGrfx()
