# ArrayCommands01.py
# This program reviews the <len> function which was
# the first array command shown in this chapter.


names = ["John","Greg","Maria","Heidi","Diana","David"]

print()
print("There are",len(names),"names in the array.")
print()

for k in range(len(names)):
   print(names[k], end = " ")
print()
   