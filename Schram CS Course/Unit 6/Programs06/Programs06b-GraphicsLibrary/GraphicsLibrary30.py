# GraphicsLibrary30.py
# This program fixes the problem of the previous program
# by using <str> to convert the number to a string.
# Now it can be concatenated with other strings.


from Graphics import *

beginGrfx(1300,700)

setColor("red")
fillOval(650,350,600,300)
setColor("white")

average = (10 + 20 + 30 + 40) / 4
drawString("The average is "+str(average),105,400,"Arial",72,"bold")

endGrfx()
