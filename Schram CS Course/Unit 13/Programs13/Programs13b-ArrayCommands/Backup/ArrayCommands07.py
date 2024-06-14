# ArrayCommands07.py
# This program demonstrates that if the same item is in the
# array more than once, the <index> command will only find 
# the "index" of the first occurrence and the <remove> command  
# will only "remove" the first occurrence from the array.


names = ["John","Greg","Maria","Heidi","David","Diana","David"]

print()
print(names)

print("\nDavid is located at index",names.index("David"))
names.remove("David")

print()
print(names)

print("\nDavid is located at index",names.index("David"))
