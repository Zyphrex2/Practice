# TurtleGraphics19.py
# This program imports the <sleep> command from
# the <time> library which allows you to make
# the turtle pause or "sleep" for a specified
# number of seconds.  Now each square stays on
# the screen for a full second before it is erased.


from turtle import *
from time import sleep

setup(800,600)

penup()       
left(135)     # face North-West
forward(350)  # Move to top-left corner
right(135)    # face East again
pendown() 

# draw square
forward(200)  
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)

sleep(1)
clear()

penup()
forward(300)  # Move to top-right corner
pendown()

# draw square
forward(200)  
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)

sleep(1)
clear()

penup()
right(90)     # face South
forward(300)  # Move to bottom-right corner
left(90)      # face East again
pendown()

# draw square
forward(200)  
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)

sleep(1)
clear()

penup()
backward(300) # Move to bottom-left corner
pendown()

# draw square
forward(200)  
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)

sleep(1)
clear()

update()
done()