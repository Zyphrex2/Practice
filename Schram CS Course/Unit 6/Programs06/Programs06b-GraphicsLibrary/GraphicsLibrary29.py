# GraphicsLibrary29.py
# This program demonstrates that the concatenation 
# trick does not work if one of the pieces of 
# information is a number.


from Graphics import *

beginGrfx(1300,700)

setColor("red")
fillOval(650,350,600,300)
setColor("white")

average = (10 + 20 + 30 + 40) / 4
drawString("The average is "+average,105,400,"Arial",72,"bold")

endGrfx()
