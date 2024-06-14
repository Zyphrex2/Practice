# GraphicsLibrary20.py
# This program demonstrates that the different polygons 
# in your program can be filled with different colors.



from Graphics import *

beginGrfx(1000,650)

drawCircle(500,100,50)
drawLine(500,150,500,400)
drawLine(500,400,400,600)
drawLine(500,400,600,600)
drawLine(300,225,700,225)
setColor("blue")	
fillPolygon([425,375,425,425,350,550,450,600,500,450,550,600,650,550,575,425,575,375])
setColor("red")
fillPolygon([350,200,650,200,650,250,575,250,575,350,425,350,425,250,350,250])

endGrfx()
