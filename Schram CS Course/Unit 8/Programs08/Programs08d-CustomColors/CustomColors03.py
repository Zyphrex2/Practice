# CustomColors03.py
# This program uses the <setColor> procedure 
# to show 256 shades of red, green and blue.  
# This creates a "shading" effect which 
# results in an illusion of depth.


from Graphics import *

beginGrfx(1300,700)

x = 150;
for red in range(256):
   setColor(red,0,0)
   drawLine(x,0,x,700)
   x += 1
   
x = 525;
for green in range(256):
   setColor(0,green,0)
   drawLine(x,0,x,700)
   x += 1
    
x = 900;
for blue in range(256):
   setColor(0,0,blue)
   drawLine(x,0,x,700)
   x += 1 
   
endGrfx()
