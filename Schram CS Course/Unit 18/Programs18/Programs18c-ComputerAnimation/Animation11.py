# Animation11.py
# This program fixes all of the issues of the
# previous program by using the <clear> command 
# to completely erase everything on the screen.  


from Graphics import *


beginGrfx(1300,700)

for x in range(35,1176,5):
   setColor("red")
   fillArc(x+50,350,75,25,270,90) # draw body
   fillArc(x+25,350,50,50,270,90) # draw hood
   setColor("black")
   fillCircle(x,350,15)           # draw rear wheel
   fillCircle(x+100,350,15)       # draw front wheel
   delay(10)
   clear()                        # erase everything

endGrfx()
