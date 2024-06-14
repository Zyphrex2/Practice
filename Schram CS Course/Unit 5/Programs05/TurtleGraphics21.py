# TurtleGraphics21.py
# This program draws the same shapes from the 
# previous program, but uses a <clear> command 
# after each shape is drawn.  Note how clearing
# the window in this manner has no effect on 
# the shape's location, orientation or width.

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
clear()

#triangle
forward(200)
left(120)
forward(200)
left(120)
forward(200)

sleep(1)
clear()

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
clear()

update()
done()
