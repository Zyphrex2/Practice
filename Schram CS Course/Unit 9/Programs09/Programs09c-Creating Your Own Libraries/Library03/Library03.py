# Library03.py
# This program has the same output as GraphicsProcedures08.py
# It demonstrates that multiple user-created libraries can
# be imported from the same file.  Breaking up a program in
# this manner makes things more organized and less cluttered.


from Graphics import *
from House import *
from Tree import *
from Background import *


beginGrfx(1000,650)

drawSky()
drawGrass()
drawFloors()
drawRoof()
drawChimney()
drawDoor()
drawWindows()
drawTrunk()
drawLeaves()

endGrfx()