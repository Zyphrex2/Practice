# GraphicsLibrary19.py
# This program demonstrates the <fillPolygon> 
# procedure of the <Graphics> library.  
# The arguments for <fillPolygon> are 
# exactly the same as for <drawPolygon>.


from Graphics import *

beginGrfx(1300,700)

fillPolygon([500,100,800,200,600,400,400,400,200,200])
fillPolygon([900,400,1000,200,1100,400,1000,600])

endGrfx()
