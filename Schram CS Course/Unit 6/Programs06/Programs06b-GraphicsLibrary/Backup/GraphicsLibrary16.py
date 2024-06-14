# GraphicsLibrary16.py
# This program demonstrates the <fillRectangle> 
# procedure of the <Graphics> library.  The 
# arguments for <fillRectangle> are exactly 
# the same as <drawRectangle>.  Even though 
# 6 solid rectangles are drawn, only 4 show 
# up on the screen.  Where are the other 2?


from Graphics import *

beginGrfx(1300,700)

fillRectangle(100,100,200,200)
fillRectangle(400,100,900,200)
fillRectangle(100,300,900,600)
fillRectangle(1000,100,1200,600)
fillRectangle(200,400,400,500)
fillRectangle(600,400,800,500)

endGrfx()
