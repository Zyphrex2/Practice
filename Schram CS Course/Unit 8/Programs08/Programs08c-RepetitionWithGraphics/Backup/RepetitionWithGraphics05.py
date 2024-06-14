# RepetitionWithGraphics05.py
# This program draws horizontal lines because 
# <y1> and <y2> are always equal.


from Graphics import *

beginGrfx(1300,700)

x1 = 100
y1 = 100
x2 = 1200
y2 = 100

for k in range(26):
   drawLine(x1,y1,x2,y2)
   y1 += 20
   y2 += 20
   
endGrfx() 
  