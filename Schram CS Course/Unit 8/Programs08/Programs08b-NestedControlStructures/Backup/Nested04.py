# Nested04.java
# This program displays a better times table  
# where everything lines up properly by using
# the <format> command.


print()

for r in range(1,16):
   for c in range(1,16):
      print("{:3}".format(r * c), end = " ")
   print()   
   