# ParameterProcedures02.py
# This program demonstrates that an argument 
# can be: a constant, like <100> or <pi>, 
# a variable, like <x>, an expression with 
# constants and/or variables, like <20 + 30> or
# <4 * x>, and a function call like <sqrt(225)>.


from math import *


def displayNumber(num): 
   print()
   print("The number is",num)
   


##########
#  MAIN  #
##########

x = 200
displayNumber(100)  
displayNumber(x)  
displayNumber(20 + 30)
displayNumber(4 * x)
displayNumber(pi)
displayNumber(sqrt(225))
 