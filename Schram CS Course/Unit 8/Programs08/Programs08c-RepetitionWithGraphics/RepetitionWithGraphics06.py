# RepetitionWithGraphics06.py
# This program draws parallel diagonal lines 
# and changes all 4 variables.


from Graphics import *

beginGrfx(1300,700)

x1 = 100
y1 = 50
x2 = 300
y2 = 350

for k in range(31):
   drawLine(x1,y1,x2,y2)
   x1 += 30
   x2 += 30
   y1 += 10
   y2 += 10
   
endGrfx()  
 