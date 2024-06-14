# Animation06.py
# This program makes the animation smoother 
# by using a smaller delay and a smaller 
# increment in the <for> loop.


from Graphics import *


beginGrfx(1300,700)

for x in range(50,1251,10):
   setColor("black")
   fillCircle(x,350,25)
   delay(100)
   setColor("white")
   fillCircle(x,350,27)

endGrfx()
