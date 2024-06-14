# Lab13Ast.py
# "Array Average" 
# This is the student, starting version of Lab 13A.
# Students need to write the <computeAverage> function.
# NOTE: This lab is meant for students in REGULAR CS1.
#       Students in CS1-HONORS will do Lab 13B.


from random import *


sum = "shadowed" 
# prevents the use of this built-in function


def heading():
   print()
   print("**********************************")
   print("Lab 13A, Array Average")
   print("100 Point Version")
   print("By: DAVID BARDAN") # Substitute your own name here.
   print("**********************************")
   print("\n")


def buildArray():
   # Specifying a seed creates "pseudo random" numbers 
   # that are the same with every program execution.
   seed(100)
   for k in range(amount):
      numbers.append(randint(10,99))  


def displayArray():
   print()
   print(numbers)
   print()
   

def computeAverage():
   x=0
   for i in numbers:
      x+=i
   x/=len(numbers)
   round(x,1)
   return x

##########
#  MAIN  #
##########

heading()
numbers = []
amount = eval(input("How many numbers do you want to generate?  -->  "))
buildArray()
displayArray()
print("Average:  ",computeAverage())

