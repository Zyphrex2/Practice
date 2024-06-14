# Functions05.py
# This program demonstrates 3 proper ways 
# and 1 improper way to call a function.


def add(n1,n2):
   return n1 + n2


   
##########
#  MAIN  #
##########

print()
print("Sum:",add(200,300))

sum = add(400,500)
print("Sum:",sum)

checking = 600
savings  = 700
if add(checking,savings) <= 0:
   print("We are broke!")
else:
   print("Let's go shopping!")   
   
add(800,900)  # Essentially does nothing   
