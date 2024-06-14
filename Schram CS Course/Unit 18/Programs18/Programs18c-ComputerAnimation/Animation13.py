# Animation13.py
# This program is similar to Animation07.py, 
# but now the circle is white and the 
# background color is black.  This means 
# <"black"> is now the "erasing color".


from Graphics import *


beginGrfx(1300,700)

setBackground("black")

for x in range(50,1251,1):
   setColor("white")
   fillCircle(x,350,25)
   delay(10)
   setColor("black")
   fillCircle(x,350,27) 

endGrfx()
