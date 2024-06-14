# Library02.py
# This program has the same output as GraphicsProcedures04.py
# The difference is all of the procedures are now in a
# user-created library called <House> which is located
# in the file House.py

# NOTE: Technically, we do not need to import <Graphics> 
# because it is already imported by the <House> library.


from Graphics import *
from House import *


beginGrfx(750,500)

drawFloors()
drawRoof()
drawChimney()
drawDoor()
drawWindows()

endGrfx()
