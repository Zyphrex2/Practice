# TurtleGraphics22.py
# This program replaces the <clear> commands 
# of the previous program with <reset>.  
# The <reset> command does more than clear the
# screen.  It also returns the turtle back to 
# the center of the screen and makes it face 
# right, sets the <width> value back to 1, 
# and sets the <color> value back to "black".

from turtle import *
from time import sleep

setup(800,600)
width(10)
color("red")

# rectangle
backward(200)
forward(400)
right(90)
forward(200)
right(90)
forward(400)
right(90)
forward(200)

sleep(1)
reset()

#triangle
forward(200)
left(120)
forward(200)
left(120)
forward(200)

sleep(1)
reset()

# star
forward(200)
right(144)
forward(200)
right(144)
forward(200)
right(144)
forward(200)
right(144)
forward(200)
right(144)

sleep(1)
reset()

update()
done()
