# GraphicsLibrary04.py
# This program combines lines, rectangles  
# and a point to draw a simple house.


from Graphics import *

beginGrfx(1000,650)

drawRectangle(100,400,450,600)
drawLine(100,400,275,300)
drawLine(450,400,275,300)
drawRectangle(255,450,405,550)
drawLine(330,450,330,550)
drawLine(255,500,405,500)
drawRectangle(140,450,210,600)
drawPoint(200,525)

endGrfx()
