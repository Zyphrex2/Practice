# Functions03.py
# This program has 2 "add" subroutines.
# <add1> is a procedure.  <add2> is a function.
# The purpose is to demonstrate the differences
# between these 2, which are:
# 1) They are called differently.
# 2) Functions end with a <return> command.


def add1(n1,n2):
   sum = n1 + n2
   print(n1,"+",n2,"=",sum)  


def add2(n1,n2):
   sum = n1 + n2
   return sum  
   

##########
#  MAIN  #
##########

num1 = 1000
num2 = 100
print()
add1(num1,num2)
print(num1,"+",num2,"=",add2(num1,num2))
