# ArrayCommands03.py
# This program uses the <append> command to build an
# array from scratch.  The empty brackets on line 9 
# indicate that <numbers> starts out as an empty array,
# which is displayed.  Then, in the <for> loop, several
# numbers are "appended" and the array is displayed again.


numbers = []

print()
print(numbers)  

for k in range(10):
   numbers.append(100 + k)

print()
print(numbers)
