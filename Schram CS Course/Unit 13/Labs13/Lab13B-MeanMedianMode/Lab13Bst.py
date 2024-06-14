# Lab13Bst.py
# "Mean, Median and Mode" 
# This is the student, starting version of Lab 13B.
# NOTE: This lab is meant for students in CS1-HONORS.
#       Students in REGULAR CS1 will do Lab 13A.


from random import *


sum = "shadowed" 
# prevents the use of this built-in function


def heading():
   print()
   print("**********************************")
   print("Lab 13B, Mean, Median and Mode")
   print("80 Point Version")
   print("By: JOHN SMITH") # Substitute your own name here.
   print("**********************************")
   print("\n")


def buildArray():
   # Specifying a seed creates "pseudo random" numbers 
   # that are the same with every program execution.
   seed(100)
   for k in range(amount):
      numbers.append(randint(10,99))  


def displayArray():
   numbers.sort()
   print()
   print(numbers)
   print()
   
   
def computeMean():
   x=0
   for i in numbers:
      x+=i
   x/=len(numbers)
   round(x,1)
   return x
   

def computeMedian():
   if len(numbers)%2 == 0:
      y = (len(numbers)/2)
      x = y - 1
      return (numbers[int(x)] + numbers[int(y)])/2
   else: return numbers[int(len(numbers)/2)]


# precondition: The <numbers> array has exactly 1 mode.
def computeMode():
   lastNumber = None
   answer = None
   lastNumberCounter = 0
   currentCounter = 0
   for i in numbers:
      if i == lastNumber:
         currentCounter += 1
         if currentCounter > lastNumberCounter:
            lastNumberCounter = currentCounter
            answer = i
      else: currentCounter = 0
      lastNumber = i
   return answer
      
   



##########
#  MAIN  #
##########

heading()
numbers = []
amount = eval(input("How many numbers do you want to generate?  -->  "))
buildArray()
displayArray()
print("Mean:  ",computeMean())
print("Median:",computeMedian())
print("Mode:  ",computeMode())
