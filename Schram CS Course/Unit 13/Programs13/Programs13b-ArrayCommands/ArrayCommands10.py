# ArrayCommands10.py
# The program uses the <in> operator check if a particular item 
# is "in" the array before attempting to find its "index".
# This prevents the program from crashing.


names = ["John","Greg","Maria","Heidi","Diana","David"]

print()
print(names)
print()

if "Heidi" in names:
   print("'Heidi' is in the list at index",names.index("Heidi"))
else:   
   print("'Heidi' is not in the list.")
print()

if "Leon" in names:
   print("'Leon' is in the list at index",names.index("Leon"))
else:   
   print("'Leon' is not in the list.")
 