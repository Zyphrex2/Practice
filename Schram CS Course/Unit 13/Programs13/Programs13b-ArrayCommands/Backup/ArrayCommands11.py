# ArrayCommands11.py
# The program uses the <in> operator check if a particular item 
# is "in" the array before attempting to "remove" it.
# This prevents the program from crashing.


names = ["John","Greg","Maria","Heidi","Diana","David"]
print()
print(names)
print()

name = input("Who do you wish to remove from the list?  -->  ")
print()

if name in names:
   names.remove(name)
   print(name,"has been removed from the list.")
   print()
   print(names)
else:   
   print(name,"was not in the list.")
