# GraphicsLibrary02.py
# This program demonstrates the <drawLine> 
# procedure of the <Graphics> library.  
# Lines are drawn from (x1,y1) to (x2,y2) 
# with <drawLine(x1,y1,x2,y2)>.  
# This program displays a snowflake by 
# calling <drawLine> 4 times.


from Graphics import *

beginGrfx(1300,700)

drawLine(650,100,650,600)
drawLine(400,350,900,350)
drawLine(450,150,850,550)
drawLine(850,150,450,550)

endGrfx()
