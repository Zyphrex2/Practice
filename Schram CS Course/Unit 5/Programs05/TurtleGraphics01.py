# TurtleGraphics01.py
# This program introduces "Turtle Graphics" by
# importing the <turtle> library and drawing a 
# single line with the <forward> command. 


# Required to have access to
# the turtle graphics commands.
import turtle 

# Specifies the dimensions of
# the Turtle Graphics window.
turtle.setup(800,600)

# Moves the "turtle" forward 100 pixels
# and draws a line in the process.
turtle.forward(100)
 
# Required to "update" the window
# when everything is drawn.
turtle.update()

# Required to keep the graphics window
# open when the program is finished.
turtle.done()
