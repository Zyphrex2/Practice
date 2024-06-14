# StringErrors06.py
# This program demonstrates what happens when you create
# substrings with index values that are too large.  
# Surprisingly, there is no error message.
# If the second number is too large, the substring will just 
# go to the end of the string, just as if it were omitted.
# If the first number is too big, the substring is simply empty.


s = "Racecar"

print()
print(s[4:])
print(s[4:10]) 
print(s[10:])
