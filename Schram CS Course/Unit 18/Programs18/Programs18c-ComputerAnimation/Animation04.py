# Animation04.py
# This program adds a short 1 second delay 
# after each circle is drawn to give you a 
# chance to see it before it is erased.
# NOTE: This is called "Draw-And-Erase Animation".
# ALSO: The issue of the circle outlines on a Mac
#       was fixed by making the radii of the 
#       erasing circles a little bigger.


from Graphics import *


beginGrfx(1300,700)

setColor("black")
fillCircle(50,350,25)
delay(1000)
setColor("white")
fillCircle(50,350,27)
      
setColor("black")
fillCircle(150,350,25)
delay(1000)
setColor("white")
fillCircle(150,350,27)
      
setColor("black")
fillCircle(250,350,25)
delay(1000)
setColor("white")
fillCircle(250,350,27)
      
setColor("black")
fillCircle(350,350,25)
delay(1000)
setColor("white")
fillCircle(350,350,27)

setColor("black")
fillCircle(450,350,25)
delay(1000)
setColor("white")
fillCircle(450,350,27)
      
setColor("black")
fillCircle(550,350,25)
delay(1000)
setColor("white")
fillCircle(550,350,27)
     
setColor("black")
fillCircle(650,350,25)
delay(1000)
setColor("white")
fillCircle(650,350,27)
      
setColor("black")
fillCircle(750,350,25)
delay(1000)
setColor("white")
fillCircle(750,350,27)
      
setColor("black")
fillCircle(850,350,25)
delay(1000)
setColor("white")
fillCircle(850,350,27)
      
setColor("black")
fillCircle(950,350,25)
delay(1000)
setColor("white")
fillCircle(950,350,27)
      
setColor("black")
fillCircle(1050,350,25)
delay(1000)
setColor("white")
fillCircle(1050,350,27)
      
setColor("black")
fillCircle(1150,350,25)
delay(1000)
setColor("white")
fillCircle(1150,350,27)
      
setColor("black")
fillCircle(1250,350,25)
delay(1000)
setColor("white")
fillCircle(1250,350,27)
        
endGrfx()
