# KeyboardInput07.py
# This program demonstrates <input> can be used with 
# graphics.  While it technically works, it is awkward 
# as you fumble between the text input in the editor 
# and the graphics output in the graphics window.


from Graphics import *

beginGrfx(1300,700)

myColor = input("Enter any color name.  -->  ")
myRadius = eval(input("Enter a radius value from 1-300.  -->  "))
setColor(myColor)
fillCircle(650,350,myRadius)

endGrfx()
