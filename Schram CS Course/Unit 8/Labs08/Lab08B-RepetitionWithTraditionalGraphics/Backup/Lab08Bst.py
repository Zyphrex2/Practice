# Lab08Bst.py
# "Repetition With Traditional Graphics"
# This is the student, starting version of Lab 08B.


from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("John Smith","8B")

# Draw Grid
drawLine(325,50,325,700)
drawLine(650,50,650,700)
drawLine(975,50,975,700)
drawLine(1300,50,1300,700)
drawLine(0,375,1300,375)
drawLine(0,700,1300,700)

# Draw Red Horizontal Lines
setColor("red")
x1 = 0
y1 = 55
x2 = 325
y2 = 55
for k in range(32):
   drawLine(x1,y1,x2,y2)
   y1 += 10
   y2 += 10


# Draw Blue Vertical Lines

 
 



# Draw Magenta Diagonal Dots

 
 
 
 

# Draw Green Concentric Circles






# Draw Purple Concentric Ovals






# Draw Brown Concentric Squares





   
# Draw Black Concentric Regular Polygons






# Draw Gold Sphere







endGrfx()
