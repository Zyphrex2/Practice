# mathLibrary04.py
# This program demonstrates what happens when 
# you take the square root of a negative number
# in Python.  It causes a Run-time Error, similar 
# to what happens when you divide by zero.  


from math import *

print()
print("Execution Begins")

n = sqrt(-1)  # invalid argument

print()
print("The square root of -1 is ",n)
