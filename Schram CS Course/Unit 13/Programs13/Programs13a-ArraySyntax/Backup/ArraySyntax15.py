# ArraySyntax15.py
# This program demonstrates that if you leave 
# out the second number in a slice, it will 
# go all of the way to the end of the array.
# It also shows that it if the second number
# is way too large, you do not get an error.
# Instead, it also goes to the end of the array.


list = [100,101,102,103,104,105,106,107,108,109]

print()
print(list)

print()
print(list[3:])

print()
print(list[3:100])
