# BigGraphicsStep04.py
# Creating a Big Graphics Program
# Step 4 - Write the next procedure, and make sure it works.
# NOTE: Make sure you remove <pass> from this procedure.


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
   pass


def drawDoor():
   pass


def drawWindows():
   pass
   
               

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