# Lab08Bst.py
# "Repetition With Traditional Graphics"
# This is the student, starting version of Lab 08B.


from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("David Bardan","8B")

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
setColor("blue")
x1 = 325
y1 = 50
x2 = 325
y2 = 375
for k in range(33):
   drawLine(x1,y1,x2,y2)
   x1 += 10
   x2 += 10
 
 



# Draw Magenta Diagonal Dots
setColor("magenta")
x = 660
y = 365
for i in range(31):
   drawPoint(x,y)
   x+=10
   y-=10
 
 
 
 

# Draw Green Concentric Circles
setColor("green")
radius = 10
for i in range(15):
   drawCircle(1137.5,212.5, radius)
   radius+=10






# Draw Purple Concentric Ovals
setColor("purple")
radius = 5
radius2 = 10
for i in range(15):
   drawOval(162.5,537.5, radius, radius2)
   radius+=5
   radius2+=10





# Draw Brown Concentric Squares
setColor("brown")
radius = 10
for i in range(23):
   drawRegularPolygon(487.5,537.5, radius, 4)
   radius+=10





   
# Draw Black Concentric Regular Polygons
setColor("black")
radius = 20
sidect = 3
for i in range(8):
   drawRegularPolygon(812.5,537.5, radius, sidect)
   radius+=20
   sidect+=1





# Draw Gold Sphere
setColor("gold")
radius = 140
radius2 = 5
for i in range(20):
   drawOval(1137.5, 537.5, radius2, radius)
   drawOval(1137.5, 537.5, radius, radius2)
   radius2+=7
   





endGrfx()
