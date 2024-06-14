# Lab06Cst.py
# "The Graphics Library Program II"
# This is the student, starting version of Lab 06C.


from textwrap import fill
from Graphics import *

beginGrfx(1300,700)

# Substitute your own name here.
drawHeading("David Bardan","6C")

fillRectangle(1192, 150, 1208, 705)
setColor("red")
fillRegularPolygon(1200, 150, 100, 8)

setColor("black")
drawRectangle(600,125,1000,300)
drawPolygon([600, 125, 800, 50, 1000, 125])
drawRectangle(650,160,750,300)
drawRectangle(800, 160, 950, 250)
drawLine(875, 160, 875, 250)
drawLine(800, 205, 950, 205)
fillCircle(735, 230, 5)

drawRectangle(500, 350, 1000, 675)
setColor("blue")
fillRectangle(500, 350, 650, 675)
setColor("red")
fillRectangle(651, 512.5, 1000, 675)
setColor("white")
fillStar(575, 512.5, 50, 5)

setColor("black")
fillCircle(200,350,25)
fillArc(260,350,40,40,135,45)
fillArc(200,290,40,40,45,315)
fillArc(200,410,40,40,225,135)
fillArc(140,350,40,40,315,225)

drawCircle(375,625,75)
drawCircle(375, 500, 50)
drawCircle(375,420,30)
drawPoint(375,500)
drawPoint(375,517.5)
drawPoint(375,535)
drawPoint(375,482.5)
drawPoint(375,465)
drawPoint(365,415)
drawPoint(385,415)
drawLine(360,430,390,430)
fillPolygon([340,400,340,390,355,390,355,360,395,360,395,390,410,390,410,400])
drawLine(325,500,275,450)
drawLine(425,500,475,450)

drawCircle(100,600,100)
drawPolygon([100,700,0,600,170,530])
drawCircle(84,617.5,47.5)

fillPolygon([10,75,55,75,55,90,25,90,25,105,40,105,40,120,25,120,25,135,55,135,55,150,10,150])
fillRectangle(70,75,85,105)
fillRectangle(100,75,115,105)
fillRectangle(85,105,100,120)
fillRectangle(70,120,85,150)
fillRectangle(100,120,115,150)
fillRectangle(130,75,145,150)
fillRectangle(145,75,175,90)
fillRectangle(145,105,175,120)
fillRectangle(160,75,175,120)
fillCircle(230,115,40)
setColor("white")
fillCircle(230,115,20)

endGrfx()
