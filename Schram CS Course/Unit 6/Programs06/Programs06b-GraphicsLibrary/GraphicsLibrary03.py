# GraphicsLibrary03.py
# This program demonstrates the <drawRectangle> 
# procedure of the <Graphics> library.  
# Rectangles are drawn from the upper-left-hand 
# corner(x1,y1) to the lower-right-hand corner
# (x2,x2) with <drawRectangle(x1,y1,x2,y2)>.


from Graphics import *

beginGrfx(1300,700)

drawRectangle(100,100,200,200)
drawRectangle(400,100,900,200)
drawRectangle(100,300,900,600)
drawRectangle(1000,100,1200,600)
drawRectangle(200,400,400,500)
drawRectangle(600,400,800,500)

endGrfx()
