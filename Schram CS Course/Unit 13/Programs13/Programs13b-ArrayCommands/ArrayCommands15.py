# ArrayCommands15.py   
# This program demonstrates that <pop> actually
# returns the removed item.  <del> does not do this.

names = ["John","Greg","Maria","Heidi","Mike","Diana","David"]
print()
print(names)

print()
print(names.pop(0))
print(names)

print()
print(names.pop(3))
print(names)

print()
print(names.pop())  # Removes the last element
print(names)