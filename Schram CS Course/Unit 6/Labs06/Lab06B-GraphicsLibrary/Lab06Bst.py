# Lab06Bst.py
# "The Graphics Library Program"
# This is the student, starting version of Lab 06B.

     
from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("David Bardan","6B")
 

      
# DRAW CUBE
drawRectangle(25,75,225,275)
drawRectangle(90,140,360,410)
drawLine(25,75,90,140)
drawLine(225,75,360,140)
drawLine(25,275,90,410)
drawLine(225,275,360,410)

# DRAW TARGET
fillCircle(550,250,125)
setColor("white")
fillCircle(550,250,100)
setColor("blue")
fillCircle(550,250,75)
setColor("red")
fillCircle(550,250,50)
setColor("yellow")
fillCircle(550,250,25)
setColor("black")


# DRAW 7-SIDED DESIGN
fillRegularPolygon(900,250,150,7)
setColor("white")
fillStar(900,250,150,7)
setColor("black")
drawBurst(900,250,150,7)


# DRAW STOPLIGHT
fillRectangle(1150,100,1250,400)
setColor("red")
fillCircle(1200,150,40)
setColor("yellow")
fillCircle(1200,250,40)
setColor("green")
fillCircle(1200,350,40)
setColor("black")
fillRectangle(1195,400,1205,702)


# DRAW JPIIHS



# DRAW SMILEY FACE
drawOval(700,500,100,140)
drawOval(660,450,35,20)
drawOval(740,450,35,20)
drawPoint(660,450)
drawPoint(740,450)
drawArc(700,525,80,30,90,270)
drawArc(660,435,35,20,280,80)
drawArc(740,435,35,20,280,80)


# DRAW WEIRD TRIANGLE
drawPolygon([900,640,1000,400,1100,640])
drawLine(1000,400,1000,640)
drawLine(950,520,1100,640)
drawLine(1050,520,900,640)



endGrfx()
