# GraphicsLibrary13.py
# This program demonstrates that the sequence of 
# the coordinate pairs is significant.  The same 
# coordinates from the previous program are used 
# in a different sequence.  The result is that 
# the display is now very different.


from Graphics import *

beginGrfx(1300,700)

drawPolygon([400,400,500,100,800,200,200,200,600,400])
drawPolygon([900,400,1000,200,1000,600,1100,400])

endGrfx()
