# TurtleGraphics16.py
# This program tries to draw 4 separate squares.
# Before each square is drawn; the "turtle" moves
# to one of the corners of the graphics window.
# The problem is the turtle is always drawing
# a several lines are drawn that we do not want.


from turtle import *

setup(800,600)

left(135)     # face North-West
forward(350)  # Move to top-left corner
right(135)    # face East again

# draw square
forward(200)  
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)

forward(300)  # Move to top-right corner

# draw square
forward(200)  
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)

right(90)     # face South
forward(300)  # Move to bottom-right corner
left(90)      # face East again

# draw square
forward(200)  
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)

backward(300) # Move to bottom-left corner

# draw square
forward(200)  
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)

update()
done()
