# mathLibrary02.py
# This program shows several different arguments 
# that can be used with the <sqrt> function.
# Note how one function call can be the argument 
# of another function call.


from math import *

n1 = sqrt(1024)		 # constant argument
n2 = sqrt(n1)			 # variable argument
n3 = sqrt(n1 + n2)    # expression argument
n4 = sqrt(sqrt(256))  # function argument

print()
print("n1:",n1)
print("n2:",n2)
print("n3:",n3)
print("n4:",n4)
