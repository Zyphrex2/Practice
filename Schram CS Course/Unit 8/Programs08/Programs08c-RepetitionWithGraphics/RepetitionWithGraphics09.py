# RepetitionWithGraphics09.py
# This program demonstrates several concentric stars.
# Each new star has 2 more points and double the radius
# of the previous star.


from Graphics import *

beginGrfx(700,700)

x = 350
y = 350
r = 20
p = 6

for k in range(5):
   drawStar(x,y,r,p)
   p += 2
   r *= 2
   
endGrfx()  
 