# Animation10.py
# This program properly animates the car across the 
# screen by placing all 4 shapes in the same <for> loop.
# A little algebra is required since the location of 3 
# of the shapes is relative to the location of the rear 
# wheel.  This program also introduces another issue.  
# As more and more images are drawn/erased on/from the 
# screen, the output gets slower and slower and eventually 
# drags to a crawl.  And on top of all of this, on a Mac 
# the car may leave behind a trail.



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
   setColor("white")
   fillArc(x+50,350,75,25,270,90) # erase body
   fillArc(x+25,350,50,50,270,90) # erase hood
   fillCircle(x,350,15)           # erase rear wheel
   fillCircle(x+100,350,15)       # erase front wheel
   
endGrfx()
