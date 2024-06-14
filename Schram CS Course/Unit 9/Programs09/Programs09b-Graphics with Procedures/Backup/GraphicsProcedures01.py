# GraphicsProcedures01.py
# This is a copy of TurtleGraphics03.py from Chapter 5.
# Note the repetitive code needed to draw the 4 squares.


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

update()
done()
