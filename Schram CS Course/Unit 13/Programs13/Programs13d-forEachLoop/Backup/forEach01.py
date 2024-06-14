# forEach01.py
# This program compares 2 "flexible" ways to
# "traverse" an array.  This first reviews the
# used of the <len> function.  The second uses
# the <for..each> loop which some people prefer.
# For displaying the contents of an array, both
# ways work just fine.


listA = [100,101,102,103,104,105,106,107,108,109]
print()
for k in range(len(listA)):
   print(listA[k], end = " ")
print()   


listB = [100,101,102,103,104,105,106,107,108,109]
print()
for number in listB:
   print(number, end = " ")
print()      
   