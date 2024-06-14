# Animation09.py
# This program demonstrates a common logic error 
# when students try to move complicated images 
# across the screen. The problem is each part of 
# the car is in its own separate loop.  This means 
# each part of the car moves across the screen one 
# at a time instead of all together.  On top of this,
# on a Mac each piece may leave behind a trail.


from Graphics import *


beginGrfx(1300,700)

for x in range(85,1226,10):       # body
   setColor("red")
   fillArc(x,350,75,25,270,90)
   delay(50)
   setColor("white")
   fillArc(x,350,75,25,270,90)

for x in range(60,1201,10):       # hood
   setColor("red")
   fillArc(x,350,50,50,270,90)
   delay(50)
   setColor("white")
   fillArc(x,350,50,50,270,90)

for x in range(35,1176,10):       # rear wheel
   setColor("black")
   fillCircle(x,350,15)
   delay(50)
   setColor("white")
   fillCircle(x,350,15)

for x in range(135,1276,10):      # front wheel
   setColor("black")
   fillCircle(x,350,15)
   delay(50)
   setColor("white")
   fillCircle(x,350,15)

endGrfx()
