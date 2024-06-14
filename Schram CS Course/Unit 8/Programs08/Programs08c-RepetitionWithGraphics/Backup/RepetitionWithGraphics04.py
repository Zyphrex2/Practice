# RepetitionWithGraphics04.py
# This program shows how a <for> loop can also be
# used with traditional graphics. This program draws 
# vertical lines because <x1> and <x2> are always equal.


from Graphics import *

beginGrfx(1300,700)

x1 = 100
y1 = 100
x2 = 100
y2 = 600

for k in range(56):
   drawLine(x1,y1,x2,y2)
   x1 += 20
   x2 += 20
   
endGrfx()  
 