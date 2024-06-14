# GraphicsLibrary17.py
# This program demonstrates the <setColor> 
# procedure of the <Graphics> library.  
# Now the two missing rectangles from the 
# previous program are visible.


from Graphics import *

beginGrfx(1300,700)

fillRectangle(100,100,200,200)
fillRectangle(400,100,900,200)
fillRectangle(100,300,900,600)
fillRectangle(1000,100,1200,600)
setColor("white")
fillRectangle(200,400,400,500)
fillRectangle(600,400,800,500)

endGrfx()
