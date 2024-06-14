# GraphicsLibrary22.py
# This program demonstrates the <fillRegularPolygon>  
# and <fillStar> procedures.  Both of these have the   
# same exact arguments as their "draw" counterparts.


from Graphics import *

beginGrfx(1300,700)

setColor("orange")
fillStar(200,200,130,5)
setColor("gold")
fillStar(500,200,130,6)
setColor("brown")
fillStar(800,200,130,7)
setColor("pink")
fillStar(1100,200,130,8)
setColor("blue")
fillRegularPolygon(200,500,130,5)
setColor("purple")
fillRegularPolygon(500,500,130,6)
setColor("green")
fillRegularPolygon(800,500,130,7)
setColor("red")
fillRegularPolygon(1100,500,130,8)

endGrfx()
