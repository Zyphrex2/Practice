# mathLibrary12.py
# The secret to "normal rounding" is to use the
# <floor> function and add .5 to the argument.


from math import *

print()
print('5.999 rounded normally is',floor(5.999 + .5))
print('5.501 rounded normally is',floor(5.501 + .5))
print('5.5   rounded normally is',floor(5.5   + .5))
print('5.499 rounded normally is',floor(5.499 + .5))
print('5.001 rounded normally is',floor(5.001 + .5))

print()
print('6.999 rounded normally is',floor(6.999 + .5))
print('6.501 rounded normally is',floor(6.501 + .5))
print('6.5   rounded normally is',floor(6.5   + .5))
print('6.499 rounded normally is',floor(6.499 + .5))
print('6.001 rounded normally is',floor(6.001 + .5))
