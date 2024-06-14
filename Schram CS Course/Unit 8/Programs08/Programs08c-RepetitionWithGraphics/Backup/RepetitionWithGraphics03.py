# RepetitionWithGraphics03.py
# This program takes the "square loop" from the
# previous program and "nests" it inside another
# <for> loop to create a special design.


from turtle import *

setup(800,600)

for j in range(8):
   for k in range(4):
      forward(200)
      right(90)
   left(45)   
 
update()
done()  
