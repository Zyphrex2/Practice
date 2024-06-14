# ArraySyntax05.py
# This program demonstrates a more flexible way to
# "traverse" an array by using the <len> function.
# NOTE: Now see what happens when you add or
#       remove names from the <names> array.


names = ["John","Greg","Maria","Heidi","Diana","David"]

print()
print("There are",len(names),"names in the array.")
print()

for k in range(len(names)):
   print(names[k], end = " ")
print()
    