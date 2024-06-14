# Nested03.java
# This program displays a times table  
# that goes from 1 * 1 to 15 * 15.   
# In this program, the table does not 
# line up properly.


print()

for r in range(1,16):
   for c in range(1,16):
      print(r * c, end = " ")
   print()   
   