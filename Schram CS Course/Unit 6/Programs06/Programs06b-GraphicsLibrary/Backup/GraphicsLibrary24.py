# GraphicsLibrary24.py
# This program demonstrates that the <width> 
# command from "Turtle Graphics" can also be 
# used with commands from the <Graphics> library.


from Graphics import *

beginGrfx(1300,700)

width(10)
drawRectangle(100,400,450,600)
drawLine(100,400,275,300)
drawLine(450,400,275,300)
drawRectangle(255,450,405,550)
drawLine(330,450,330,550)
drawLine(255,500,405,500)
drawRectangle(140,450,210,600)
drawPoint(195,525)

width(20)
drawCircle(500,200,130)
drawStar(800,200,130,5)
drawBurst(1100,200,130,15)

width(30)
drawOval(715,500,190,100)
drawRegularPolygon(1100,500,130,7)

width(1) # back to default
drawPolygon([50,50,250,50,180,150,250,250,50,250,120,150])

endGrfx()
