# Animation08.py
# This program draws the car that will  
# be animated in the next few programs.  
# The car is an overlapping composition
# of 4 filled shapes, specifically the 
# 2 arcs and 2 circles.


from Graphics import *


beginGrfx(1300,700)

setColor("red")
fillArc(85,350,75,25,270,90)  # body
fillArc(60,350,50,50,270,90)  # hood
setColor("black")
fillCircle(35,350,15)         # rear wheel
fillCircle(135,350,15)        # front wheel

endGrfx()
