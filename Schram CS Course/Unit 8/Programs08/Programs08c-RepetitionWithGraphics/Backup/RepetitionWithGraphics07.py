# RepetitionWithGraphics07.py
# This program demonstrates several lines with the same
# starting point. In this case the (x1,y1) coordinate
# stays fixed while the (x2,y2) point changes.


from Graphics import *

beginGrfx(1300,700)

x1 = 100
y1 = 100
x2 = 1200
y2 = 100

for k in range(26):
   drawLine(x1,y1,x2,y2)
   x2 -= 35
   y2 += 20
   
endGrfx()   
