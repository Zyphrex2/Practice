# Functions01.py
# This program introduces a "function" with one parameter.
# Function <getNextNumber> returns the next integer value 
# of its parameter
# NOTE: A function is a subroutine that returns a value.
# A procedure is a subroutine that does not return a value.


from random import randint


def getNextNumber(current):
   next = current + 1
   return next
   
   

##########
#  MAIN  #
##########

for k in range(10):
   randNum = randint(10,99)
   print()
   print("Random number:",randNum)
   print("Next number:  ",getNextNumber(randNum))
