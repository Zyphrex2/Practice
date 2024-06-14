# GraphicsLibrary25.py
# This program demonstrates the <drawString> 
# procedure of the <Graphics> library.  With 
# <drawString("Hello World",x,y)>, the string 
# "Hello World" will be displayed starting at 
# coordinate (x,y).


from Graphics import *

beginGrfx(1300,700)

drawString("Top-Left-Hand Corner",10,30)
drawString("Top-Right-Hand Corner",1120,30)
drawString("Bottom-Left-Hand Corner",10,690)
drawString("Bottom-Right-Hand Corner",1100,690)
drawString("Middle",630,355)

endGrfx()
