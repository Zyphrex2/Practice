# GraphicsProcedures02.py
# This program has the same output as the previous 
# program but is more efficient because a special 
# <drawSquare> procedure has been created which 
# eliminates the repetitive code.


from turtle import *


def drawSquare():
   pendown()
   forward(200)  
   right(90)
   forward(200)
   right(90)
   forward(200)
   right(90)
   forward(200)
   right(90)
   penup()



##########
#  MAIN  #
##########

setup(800,600)

penup()       
left(135)     # face North-West
forward(350)  # Move to top-left corner
right(135)    # face East again

drawSquare()

forward(300)  # Move to top-right corner

drawSquare()

right(90)     # face South
forward(300)  # Move to bottom-right corner
left(90)      # face East again

drawSquare()

backward(300) # Move to bottom-left corner

drawSquare()

update()
done()
