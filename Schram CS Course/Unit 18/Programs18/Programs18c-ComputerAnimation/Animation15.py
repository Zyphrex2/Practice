# Animation15.py
# This program fixes the "slowing down" problem
# of the previous program by using <clear>.  
# This does require that the background color 
# is set immediately after the <clear> command.
# NOTE: This is called "Draw-And-Redraw Animation".


from Graphics import *


beginGrfx(1300,700)



for x in range(50,51,3):
   clear()
   setBackground("black")
   setColor("white")
   fillCircle(x,315,15)
   fillCircle(x,350,25)
   fillCircle(x,405,40)
   delay(10)

endGrfx()
