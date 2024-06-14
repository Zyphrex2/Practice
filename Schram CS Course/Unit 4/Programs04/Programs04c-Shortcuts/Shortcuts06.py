# Shortcuts06.py
# This program demonstrates that the <+=> 
# shortcut can be used with strings to join 
# a string value to the end of an existing 
# string.  This means that <+=> is also an 
# "Overloaded Operator".


name = "John"
name += "Public"
print()
print(name)

name = "John"
space = ' '
name += space
name += "Public"
print()
print(name)

name = "John"
name += space
name += 'Q'
name += '.'
name += space
name += "Public"
print()
print(name)
