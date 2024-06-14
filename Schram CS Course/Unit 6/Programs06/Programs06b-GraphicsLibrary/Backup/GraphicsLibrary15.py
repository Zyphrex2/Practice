# GraphicsLibrary15.py
# This program demonstrates the <drawStar> and <drawBurst> 
# procedures of the <Graphics> library.  Stars and bursts 
# are drawn from their center (x,y) with a certain radius 
# (of the circumscribing circle) and a certain number of 
# points/lines with <drawStar(x,y,radius,numPoints)>
# and <drawBurst(x,y,radius,numLines)>.


from Graphics import *

beginGrfx(1300,700)

drawStar(200,200,130,5)
drawStar(500,200,130,6)
drawStar(800,200,130,7)
drawStar(1100,200,130,8)
drawBurst(200,500,130,5)
drawBurst(500,500,130,6)
drawBurst(800,500,130,7)
drawBurst(1100,500,130,8)

endGrfx()
