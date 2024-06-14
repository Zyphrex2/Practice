# Selection13.py
# This program demonstrates that selection can be used
# to manipulate the output of a graphics program.
# This is the very thing you will be doing in Lab 7B.


from Graphics import *

beginGrfx(1300,700)

shapeNum = numinput("Shape Selection","1 = Circle \n2 = Star")

if shapeNum == 1:
   fillCircle(650,350,250)
elif shapeNum == 2:
   fillStar(650,350,250,8)
else:
   drawString("You did not enter a 1 or a 2.",100,315,"Arial",48,"bold")   
   drawString("Please try again.",100,465,"Arial",48,"bold")   
   
endGrfx()