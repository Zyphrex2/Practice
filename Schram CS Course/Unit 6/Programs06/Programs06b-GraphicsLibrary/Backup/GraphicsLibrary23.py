# GraphicsLibrary23.py
# This program demonstrates <fillOval> and <fillArc>.
# In the same way that an arc is a piece of an oval
# a "filled arc" is a piece of a "filled oval".


from Graphics import *

beginGrfx(1300,700)

fillOval(200,200,100,130)
fillOval(500,200,130,70)
fillOval(800,200,40,130)
setColor("yellow")
fillOval(1100,200,130,130)
setColor("black")
drawLine(1100,200,1230,200)
drawPoint(1120,120)
fillArc(200,500,100,130,270,360)
fillArc(500,500,130,70,90,270)
fillArc(800,500,40,130,0,180)
setColor("yellow")
fillArc(1100,500,130,130,135,45)
setColor("black")
drawPoint(1120,420)

endGrfx()
