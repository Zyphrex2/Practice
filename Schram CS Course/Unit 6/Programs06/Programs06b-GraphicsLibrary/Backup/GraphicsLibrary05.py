# GraphicsLibrary05.py
# This program demonstrates the Logic Error 
# that occurs when X and Y values are switched.  
# The house is "flipped" diagonally.


from Graphics import *

beginGrfx(1000,650)

drawRectangle(400,100,600,450)
drawLine(400,100,300,275)
drawLine(400,450,300,275)
drawRectangle(450,255,550,405)
drawLine(450,330,550,330)
drawLine(500,255,500,405)
drawRectangle(450,140,600,210)
drawPoint(525,200)

endGrfx()
