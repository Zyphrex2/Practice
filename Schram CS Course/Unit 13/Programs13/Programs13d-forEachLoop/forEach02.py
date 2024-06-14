# forEach02.py
# This program does another comparison between
# the <for> loop and the <for..each> loop.  
# This time, the mission is to change all 
# of the numbers in both arrays to 500.
# The output shows that the <for..each> loop is
# not able to change the contents of an array.


listA = [100,101,102,103,104,105,106,107,108,109]
for k in range(len(listA)):
   listA[k] = 500

listB = [100,101,102,103,104,105,106,107,108,109]
for number in listB:
   number = 500
  
print()  
print(listA)  
print()  
print(listB)    
   