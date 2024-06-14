# BigGraphicsStep03.py
# Creating a Big Graphics Program
# Step 3 - Write the first procedure, and make sure it works.
# NOTE: Make sure you remove <pass> from this procedure.


from Graphics import *


def drawFloors():
   setColor("blue")
   drawRectangle(200,200,500,300)
   drawRectangle(200,300,500,400)


def drawRoof():
   pass


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