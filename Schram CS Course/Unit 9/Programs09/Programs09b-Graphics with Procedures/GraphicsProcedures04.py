# GraphicsProcedures04.py
# This program divides the house up into several
# different procedures.  Imagine again that you 
# want to change the appearance of the chimney.
# Finding the appropriate code is much easier now.
# NOTE: The "MAIN" section of the program now looks
#       like an outline.


from Graphics import *


def drawFloors():
   setColor("blue")
   drawRectangle(200,200,500,300)
   drawRectangle(200,300,500,400)


def drawRoof():
   setColor("red")
   drawLine(200,200,350,100)
   drawLine(500,200,350,100)
   drawLine(200,200,500,200)


def drawChimney():
   drawLine(420,146,420,80)
   drawLine(420,80,450,80)
   drawLine(450,80,450,166)


def drawDoor():
   setColor("black")
   drawRectangle(330,340,370,400)
   drawOval(350,370,10,20)
   fillCircle(366,370,3)


def drawWindows():
   drawRectangle(220,220,280,280)
   drawLine(220,250,280,250)
   drawLine(250,220,250,280)
   drawRectangle(420,220,480,280)
   drawLine(420,250,480,250)
   drawLine(450,220,450,280)
   drawRectangle(320,220,380,280)
   drawLine(320,250,380,250)
   drawLine(350,220,350,280)
   drawRectangle(220,320,280,380)
   drawLine(220,350,280,350)
   drawLine(250,320,250,380)
   drawRectangle(420,320,480,380)
   drawLine(420,350,480,350)
   drawLine(450,320,450,380)



##########
#  MAIN  #
##########

beginGrfx(750,500)

drawFloors()
drawRoof()
drawChimney()
drawDoor()
drawWindows()

endGrfx()
