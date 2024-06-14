# ParameterProcedures05.py
# This program demonstrates that argument data types also
# matter. In this example 2 string arguments were passed
# to procedure <showDifference>.  This does not work as
# "subtraction" is something that only works with numbers.


def showDifference(a,b):
   difference = a - b
   print()
   print("The difference is",difference)
   


##########
#  MAIN  #
##########

num1 = "John"
num2 = "Smith"
showDifference(num1,num2)
showDifference(num2,num1)
