# RandomNumbers02.py
# This program is more efficient and flexible than the 
# previous program.  It is more efficient because the 
# 5 <print> commands are now in a <for> loop.
# It is more flexible because the user can specify 
# the range of random numbers.


from random import randint

print()
min = eval(input("Enter the smallest number.  -->  "))
max = eval(input("Enter the largest number.   -->  "))
print()

for k in range(5):
   print(randint(min,max))
