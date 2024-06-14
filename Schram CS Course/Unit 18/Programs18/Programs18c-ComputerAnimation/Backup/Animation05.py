# Animation05.py
# This program has the same output as the 
# previous program.  The program is now much 
# shorter because it uses a <for> loop.


from Graphics import *


beginGrfx(1300,700)

for x in range(50,1251,100):
   setColor("black")
   fillCircle(x,350,25)
   delay(1000)
   setColor("white")
   fillCircle(x,350,25)

endGrfx()
