# mathLibrary07.py
# This program demonstrates the <pow> function 
# of the <math> library which does the same 
# thing as the exponent operator <**>.

# NOTE: Like <max> and <min>, <pow> uses 2 
# argument.  However, unlike <max> and <min>, 
# with <pow> the order of the 2 argument is 
# VERY significant.
# The first argument is the "base".  
# The second argument is the "exponent".
# <pow> returns the first argument to the 
# "power" of the second argument.


from math import *

print()
print("3 to the 4th power using ** is",3 ** 4)
print("3 to the 4th power with pow is",pow(3,4))
print()
print("4 to the 3rd power using ** is",4 ** 3)
print("4 to the 3rd power with pow is",pow(4,3))
