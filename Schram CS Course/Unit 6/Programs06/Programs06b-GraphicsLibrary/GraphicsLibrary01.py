# GraphicsLibrary01.py
# This program demonstrates the <drawPixel> and 
# <drawPoint> procedures of the <Graphics> library.
# Both procedures draw a dot on the computer screen.

# NOTE: The <Graphics> library was created by Mr. Schram
#       and is not part of standard Python.

# NOTE: Most of the procedures in the <Graphics> library 
#       use integer arguments.


# Required to have access to the 
# <Graphics> library commands.
from Graphics import *

# Opens a graphics window 
# with specified dimensions
beginGrfx(1300,700)

# Draws tiny individual pixels
drawPixel(100,300)
drawPixel(200,300)
drawPixel(300,300)
drawPixel(400,300)
drawPixel(500,300)
drawPixel(600,300)
drawPixel(700,300)
drawPixel(800,300)
drawPixel(900,300)
drawPixel(1000,300)
drawPixel(1100,300)
drawPixel(1200,300)

# Draws small squares
drawPoint(100,400)
drawPoint(200,400)
drawPoint(300,400)
drawPoint(400,400)
drawPoint(500,400)
drawPoint(600,400)
drawPoint(700,400)
drawPoint(800,400)
drawPoint(900,400)
drawPoint(1000,400)
drawPoint(1100,400)
drawPoint(1200,400)

# Updates the screen and keeps the graphics 
# window open when the program is finished.
endGrfx()
