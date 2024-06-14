# Lab13C
# Program:  AnalyzeArray

from random import *

def heading():
   print()
   print("**********************************")
   print("Lab 13C, Array Analyzer")
   print("By: JOHN SMITH") # Substitute your own name here.
   print("**********************************")
   print("\n")

def buildArray():
   # Specifying a seed creates "pseudo random" numbers 
   # that are the same with every program execution.
   numbers = []
   seed(100)
   for k in range(amount):
      numbers.append(randint(10,99))
   return numbers

def findMaxValue(theArray):
   maxValue = 0

   for i in theArray:
      if i > maxValue:
         maxValue = i
    
   return maxValue

def findEvenValues(theArray):
   evenArray = []

   for i in theArray:
      if i % 2 == 0:
         evenArray.append(i)
   
   return evenArray


def isStrictlyIncreasing(theArray):
   isStrictlyIncreasing = False
   lastValue = 0

   for i in theArray:
      if i > lastValue:
         isStrictlyIncreasing = True
      else: 
         isStrictlyIncreasing = False
         return isStrictlyIncreasing
      lastValue = i
   
   return isStrictlyIncreasing


#########  MAIN PROGRAM #############

heading()
amount = eval(input("How many numbers do you want to generate?  -->  "))
array1 = buildArray()

#Print the array and find the minimum and weather array is strictly increasing
print(array1)
print("Maximum Value in array: ", findMaxValue(array1))
print("Array is strictly increasing: ", isStrictlyIncreasing(array1))
theEvenNumbers = findEvenValues(array1)
print("Even Numbers: ", theEvenNumbers)

#Sort the array1 and call the functions again.
