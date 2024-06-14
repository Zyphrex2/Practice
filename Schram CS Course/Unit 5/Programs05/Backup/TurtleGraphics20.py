# TurtleGraphics20.py
# This program draws a rectangle, a triangle,
# and a star.   Note how the way one shape 
# finishes affects the location and rotation
# of the next shape.

from turtle import *

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

#triangle
forward(200)
left(120)
forward(200)
left(120)
forward(200)

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

update()
done()
