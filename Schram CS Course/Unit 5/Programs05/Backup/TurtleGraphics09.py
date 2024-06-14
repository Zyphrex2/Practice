# TurtleGraphics09.py
# This program demonstrates that turns do 
# not need to be 90 degree "right angles".
# You can turn any number of degrees.
# With 3 turns of 120 degrees, I can
# make an equilateral triangle.


from turtle import *

setup(800,600)

forward(200)
left(120)
forward(200)
left(120)
forward(200)
left(120)

update()
done()
