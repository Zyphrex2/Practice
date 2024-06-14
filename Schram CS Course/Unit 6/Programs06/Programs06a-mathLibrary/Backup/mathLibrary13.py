# mathLibrary13.py
# The program demonstrates the <trunc> function 
# which "chops-off" or "truncates" the fractional
# part of a real number.  While this may seem 
# identical to the <floor> function, it does 
# behave differently with negative numbers.


from math import *

print()
print("5.678 rounded down is",floor(5.678))
print('5.678 "truncated" is ',trunc(5.678))

print()
print("-5.678 rounded down is",floor(-5.678))
print('-5.678 "truncated" is ',trunc(-5.678))
