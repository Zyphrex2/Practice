# Functions04.py
# This program demonstrates a 4 "function" calculator.
# NOTE: While it may be good program design to put all
# of these functions in a separate library, most of the
# examples in the book will continue to put the entire
# program in a single file for the same of simplicity.


def add(n1,n2):
   return n1 + n2


def subtract(n1,n2):
   return n1 - n2
   

def multiply(n1,n2):
   return n1 * n2   


def divide(n1,n2):
   return n1 / n2
   
   
   
##########
#  MAIN  #
##########

num1 = 1000
num2 = 100
print()
print(num1,"+",num2,"=",add(num1,num2))
print(num1,"-",num2,"=",subtract(num1,num2))
print(num1,"*",num2,"=",multiply(num1,num2))
print(num1,"/",num2,"=",divide(num1,num2))
