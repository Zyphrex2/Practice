# GraphicsLibrary28.py
# This program demonstrates the proper way to display
# multiple pieces of information with <drawString>.
# The secret is to use String Concatenation to combine
# the different pieces of information into a single
# string argument.


from Graphics import *

beginGrfx(1300,700)

setColor("red")
fillOval(650,350,600,300)
setColor("white")

firstName = "John "
lastName = "Smith"
drawString("Hello "+firstName+lastName,160,400,"Arial",72,"bold")

endGrfx()
