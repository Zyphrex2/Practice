# GraphicsLibrary09.py
# This program demonstrates the <drawOval> 
# procedure of the <Graphics> library.  
# Ovals are drawn from their center (x,y) 
# with a horizontal radius (hr) and a vertical 
# radius (vr) with <drawOval(x,y,hr,vr)>.


from Graphics import *

beginGrfx(1300,700)

drawOval(225,150,100,100)
drawOval(1100,325,150,300)
drawOval(675,150,250,60)
drawOval(650,350,40,100)
drawOval(650,350,100,40)
drawOval(125,475,80,200)
drawOval(575,575,200,80)

endGrfx()
