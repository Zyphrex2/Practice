# Lab08Cvst.py
# "Random Graphics"
# This is the student, starting version of Lab 08C.


from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("John Smith","8C")

# Draw Grid
drawLine(325,50,325,700)
drawLine(650,50,650,700)
drawLine(975,50,975,700)
drawLine(1300,50,1300,700)
drawLine(0,375,1300,375)
drawLine(0,700,1300,700)

# Draw 1000 Random Points.
for k in range(1000):
   setRandomColor()
   x = randint(5,320)
   y = randint(55,370)
   drawPoint(x,y)
update()

# Draw 500 Random Lines.




# Draw 100 Random Rectangles.




# Draw 100 Random Triangles.




# Draw Your Initials 100 Times with random sizes.




# Draw 100 Random Stars with a constant radius 
# of 50 and a random # of Points.




# Draw 100 Random Circles with random radii.




# Draw 100 Random Arcs with random horizontal radii,
# vertical radii, starting points and stopping points.







endGrfx()
