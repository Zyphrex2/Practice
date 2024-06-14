from math import *
# Lab13D
# Program:  For Loop Rewriting

from random import *

def heading():
   print()
   print("**********************************")
   print("Lab 13D For Loop Rewriting")
   print("By: David Bardan") # Substitute your own name here.
   print("**********************************")
   print("\n")

def curveGrades(theGrades):
   for i in range(len(theGrades)):
      theGrades[i] = int (10 * sqrt(theGrades[i]))
   print("Grade curve complete.")
   
def averageGrades(theGrades):
   total = 0
   for grade in theGrades:
      total += grade
   average = total / len(theGrades)
   return average
   
############### MAIN PROGRAM ####################

grades = [92, 65, 50, 72, 73, 34, 100, 83, 58, 72]

print("Step 1:  Original Grades")
print(grades)
print()

print("Step 2:  Average original grades")
avg = averageGrades(grades)
print("Grade Average: ", avg)
print()

print("Step 2:  Curve the grades")
curveGrades(grades)
print(grades)
print()

print("Step 3:  Average the curved grades")
avg = averageGrades(grades)
print("Grade Average: ", avg)