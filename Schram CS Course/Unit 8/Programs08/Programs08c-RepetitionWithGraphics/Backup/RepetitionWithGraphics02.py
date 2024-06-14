# RepetitionWithGraphics02.py
# This program draws the same square as the previous 
# program, but is more efficient because it uses a 
# <for> loop to create the square.


from turtle import *

setup(800,600)

for k in range(4):
   forward(200)
   right(90)

update()
done() 
 