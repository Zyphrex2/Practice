# ParameterProcedures04.py
# This program demonstrates that argument sequence 
# matters. In this example procedure <showDifference> 
# will display different results when the calling
# argument are reversed.


def showDifference(a,b):
   difference = a - b
   print()
   print("The difference is",difference)
   


##########
#  MAIN  #
##########

num1 = 100
num2 = 50
showDifference(num1,num2)
showDifference(num2,num1)
