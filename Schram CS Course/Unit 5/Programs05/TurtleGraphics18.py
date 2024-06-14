# TurtleGraphics18.py
# This program puts a <clear> command after each
# square is drawn.  Now we only see one square
# (briefly) at a time.

from turtle import *

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

clear()

update()
done()
