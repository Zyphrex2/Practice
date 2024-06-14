# GraphicsLibrary27.py 
# This program demonstrates what happens when you try to
# display multiple pieces of information with <drawString>
# separated with commas like you do with <print>.
# This does not work because the each separate piece of
# information is its own argument.


from Graphics import *

beginGrfx(1300,700)

setColor("red")
fillOval(650,350,600,300)
setColor("white")

firstName = "John "
lastName = "Smith"
drawString("Hello ",firstName,lastName,160,400,"Arial",72,"bold")

endGrfx()
