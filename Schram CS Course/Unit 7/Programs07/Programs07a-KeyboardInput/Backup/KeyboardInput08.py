# KeyboardInput08.py
# This program demonstrates <textinput> and <numinput>
# which are better suited for graphics programs.
# Note that <numinput> does not require the <eval> function.


from Graphics import *

beginGrfx(1300,700)

myColor = textinput("Color Input","Enter any color name.")
myRadius = numinput("Radius Input","Enter a # from 1-300.")
setColor(myColor)
fillCircle(650,350,myRadius)

endGrfx()
