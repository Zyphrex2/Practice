# GraphicsLibrary14.py
# This program demonstrates the <drawRegularPolygon> 
# procedure of the <Graphics> library.  Regular Polygons 
# are drawn from their center (x,y) with a certain radius 
# (of the circumscribing circle) and a certain number of 
# sides with <drawRegularPolygon(x,y,radius,numSides)>.


from Graphics import *

beginGrfx(1300,700)

drawRegularPolygon(200,200,130,3)
drawRegularPolygon(500,200,130,4)
drawRegularPolygon(800,200,130,5)
drawRegularPolygon(1100,200,130,6)
drawRegularPolygon(200,500,130,7)
drawRegularPolygon(500,500,130,8)
drawRegularPolygon(800,500,130,9)
drawRegularPolygon(1100,500,130,10)

endGrfx()
