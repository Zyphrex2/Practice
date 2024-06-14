# mathLibrary05.py
# This program demonstrates the <abs>  
# function, which returns the absolute
# value of the argument.  It also shows
# how the <abs> function can be used to 
# prevent the issue of a negative argument
# with the <sqrt> function.


from math import *

print()
print("The absolute value of -25 is",abs(-25))
print("The absolute value of 100 is",abs(100))
print("The absolute value of 3.7 is",abs(3.7))
print("The absolute value of -.5 is",abs(-.5))
print("The absolute value of 0.0 is",abs(0.0))
print()
print("The square root of the absolute value")
print("of -256 is",sqrt(abs(-256)))
