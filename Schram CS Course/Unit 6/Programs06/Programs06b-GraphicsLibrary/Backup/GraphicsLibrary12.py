# GraphicsLibrary12.py
# This program demonstrates the <drawPolygon> procedure.
# <drawPolygon> can handle 3 or more sets of coordinate
# points to draw a triangle, quadrilateral, pentagon, 
# hexagon, octagon, or any other polygon.
# The purpose of the extra set of brackets [] in the 
# procedure call will be explained in a later chapter.


from Graphics import *

beginGrfx(1300,700)

drawPolygon([500,100,800,200,600,400,400,400,200,200])
drawPolygon([900,400,1000,200,1100,400,1000,600])

endGrfx()
