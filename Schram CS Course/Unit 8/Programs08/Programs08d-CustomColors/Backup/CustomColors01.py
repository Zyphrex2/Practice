# CustomColors01.py
# This program displays the Texas flag using the 
# built-in colors for red, white and blue.  While 
# this certainly looks like the Texas flag, it does 
# not use the official shades of red and blue that
# are used in the Official Texas Flag.


from Graphics import *

beginGrfx(1300,700)

setColor("blue")
fillRectangle(0,0,350,700)
setColor("red")
fillRectangle(350,350,1300,700)
setColor("white")
fillStar(175,350,130,5)

endGrfx()
