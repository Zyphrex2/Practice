# Repetition07.py
# This program demonstrates how to change the "step"
# value in the <for> loop.  By default it is 1.
# To count by a number other than 1 requires adding
# a third number to the <range> command.  
# NOTE: As before, you may need to add 1 to the
# "stopping value" to make the loop work properly.


print()

for k in range(10,30,2): # Displays evens from 10 to 28
   print(k, end = " ")
   
print("\n")

for k in range(10,31,2): # Displays evens from 10 to 30
   print(k, end = " ")
   
print("\n")

for k in range(5,101,5): # Displays 5 to 100 by 5s
   print(k, end = " ")
   
print("\n")

for k in range(50,81,3): # Displays 50 to 80 by 3s
   print(k, end = " ")
   
print("\n")

for k in range(20,0,-1): # Displays 20 down to 1
   print(k, end = " ")
   
print("\n")


for k in range(20,-1,-1): # Displays 20 down to 0
   print(k, end = " ") 
   
print()   
