# Lab09Bst.pv
# "Geometry Functions"
# This is the student, starting version of Lab 09B.


from math import pi


def heading():
   print()
   print("**********************************")
   print("Lab 09B, Geometry Functions")
   print("100 Point Version")
   print("By: DAVID BARDAN") # Substitute your own name here.
   print("**********************************")
   print("\n")


# 2D Perimeters
def squarePerimeter (s):
   return 4 * s
def pentagonPerimeter(s):
   return 5 * s
def hexagonPerimeter(s):
   return 6 * s
def octagonPerimeter(s):
   return 8 * s
def rectanglePerimeter(l,w):
   return 2 * (l+w)
def circleCircumference(r):
   return 2 * pi * r

# 2D Areas
def squareArea(side):
   return int(side) ** 2
def rectangleArea (L,W):
   return L * W
def parallelogramArea (b,h):
   return b * h
def triangleArea(b, h):
   return 0.5 * b * h
def trapezoidArea(b1,b2,h):
   return (b1+b2)/2*h
def hexagonArea(b1,b2,h):
   return (b1+b2)*h
def circleArea(r):
   return pi * r**2

# 3D Surface Areas
def cubeSurfaceArea (s):
   return 6 * s ** 2
def squarePrismSurfaceArea(s,h):
   return 2*s**2+4*s*h
def rectangularPrismSurfaceArea(l,w,h):
   return 2*l*w+2*l*h+2*w*h
def sphereSurfaceArea(r):
   return 4*pi*(r**2)

# 3D Volumes
def cubeVolume(s):
   return s**3
def squarePrismVolume(s,h):
   return s**2 * h
def rectangularPrismVolume(l,w,h):
   return l*w*h
def pyramidVolume(s,h):
   return 1/3*s**2*h
def cylinderVolume (r,h):
   return pi * r ** 2 * h
def coneVolume(r,h):
   return 1/3*pi*r**2*h
def sphereVolume(r):
   return 4/3*pi*r**3

##########
#  MAIN  #
##########

heading()

side   =  4.0
length =  5.0
width  =  6.0
height =  7.0
base1  =  8.0
base2  =  9.0
radius = 10.0
side = 4

# Uncomment the print statements below as you complete each of the functions.
# Leave hashtags in place for any functions that you have not yet finished.
print("Perimeters of 2D Shapes")
print("=====================================================")
print("Square Perimeter:               ",squarePerimeter(side))
print("Pentagon Perimeter:             ",pentagonPerimeter(side))
print("Hexagon Perimeter:              ",hexagonPerimeter(side))
print("Octagon Perimeter:              ",octagonPerimeter(side))
print("Rectangle Perimeter:            ",rectanglePerimeter(length,width))
print("Circle Circumference:           ",circleCircumference(radius))
print("\n")
print("Areas of 2D Shapes")
print("=====================================================")
print("Square Area:                    ",squareArea(side))
print("Rectangle Area:                 ",rectangleArea(length,width))
print("Parallelogram Area:             ",parallelogramArea(base1,height))
print("Triangle Area:                  ",triangleArea(base1,height))
print("Trapezoid Area:                 ",trapezoidArea(base1,base2,height))
print("Hexagon Area:                   ",hexagonArea(base1,base2,height))
print("Circle Area:                    ",circleArea(radius))
print("\n")
print("Surface Areas of 3D Shapes")
print("=====================================================")
print("Cube Surface Area:              ",cubeSurfaceArea(side))
print("Square Prism Surface Area:      ",squarePrismSurfaceArea(side,height))
print("Rectangular Prism Surface Area: ",rectangularPrismSurfaceArea(length,width,height))
print("Sphere Surface Area:            ",sphereSurfaceArea(radius))
print("\n")
print("Volumes of 3D Shapes")
print("=====================================================")
print("Cube Volume:                    ",cubeVolume(side))
print("Square Prism Volume:            ",squarePrismVolume(side,height))
print("Rectangular Prism Volume:       ",rectangularPrismVolume(length,width,height))
print("Pyramid Volume:                 ",pyramidVolume(side,height))
print("Cylinder Volume:                ",cylinderVolume(radius,height))
print("Cone Volume:                    ",coneVolume(radius,height))
print("Sphere Volume:                  ",sphereVolume(radius))
print()