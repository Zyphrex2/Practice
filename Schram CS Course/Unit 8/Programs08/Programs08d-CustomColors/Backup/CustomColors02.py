# CustomColors02.py
# This program demonstrates the <setColor> procedure 
# being used to "create" custom colors.  The program 
# will draw the Official Texas Flag with the EXACT 
# official shades of red and blue required.


from Graphics import *

beginGrfx(1300,700)

setColor(0,39,104)     # Texas Flag blue
fillRectangle(0,0,350,700)
setColor(190,10,47)    # Texas Flag red
fillRectangle(350,350,1300,700)
setColor(255,255,255)  # Three 255s = "white"
fillStar(175,350,130,5)

endGrfx()
