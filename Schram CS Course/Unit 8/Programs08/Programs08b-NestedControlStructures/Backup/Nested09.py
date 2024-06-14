# Nested09.py
# This program demonstrates that repetition can 
# be nested inside a selection.
# In truth, ANY control structure can be nested  
# inside ANY other control structure.
# The program also shows how to determine if a 
# number is even or odd.


print()
stop = eval(input("Enter a number between 1 and 15.  -->  "))
print()

if (stop % 2 == 0):  # if stop is even
   for k in range(stop):
      print("EVEN",end = " ")
else:                # if stop is odd
   for k in range(stop):
      print("ODD",end = " ")

print()          