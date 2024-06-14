# Lab08Cvst.py
# "Random Graphics"
# This is the student, starting version of Lab 08C.


from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("David Bardan","8C")

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
for k in range(500):
   setRandomColor()
   x = randint(325,650)
   y = randint(55,370)
   x2 = randint(325,648)
   y2= randint(55,370)
   drawLine(x,y,x2,y2)
update()



# Draw 100 Random Rectangles.
for k in range(100):
   setRandomColor()
   x = randint(652,960)
   y = randint(55,370)
   x2 = randint(652,960)
   y2= randint(55,370)
   fillRectangle(x,y,x2,y2)
update()



# Draw 100 Random Triangles.
for k in range(100):
   setRandomColor()
   x = randint(975,1300)
   y = randint(55,370)
   x2 = randint(975,1300)
   y2 = randint(55,370)
   x3 = randint(975,1300)
   y3 = randint(55,370)
   fillPolygon([x,y,x2,y2,x3,y3])
update()



# Draw Your Initials 100 Times with random sizes.
for k in range(100):
   setRandomColor()
   x = randint(0,260)
   y = randint(420,700)
   x2 = randint(10,36)
   drawString("DB", x, y, "Arial", x2)
update()



# Draw 100 Random Stars with a constant radius 
# of 50 and a random # of Points.
for k in range(100):
   setRandomColor()
   x = randint(375, 600)
   y = randint(425,650)
   x2 = randint(5,10)
   fillStar(x,y,50,x2)
update()



# Draw 100 Random Circles with random radii.
for k in range(100):
   setRandomColor()
   x = randint(725, 900)
   y = randint(450,625)
   x2 = randint(1,75)
   fillCircle(x,y,x2)
update()



# Draw 100 Random Arcs with random horizontal radii,
# vertical radii, starting points and stopping points.
for k in range(100):
   setRandomColor()
   x = randint(1050,1225)
   y = randint(450,625)
   x2 = randint(1,75)
   y2 = randint(1,75)
   x3 = randint(0,360)
   y3 = randint(0,360)
   fillArc(x,y,x2,y2,x3,y3)
update()






endGrfx()
