# StringCommands12.py
# This program fixes the "case" issue of StringOperators07.py
# by using the <upper> command.  With both strings converted
# to UPPERCASE, the strings can be compared properly.
# NOTE: Using the <lower> command would also work.

print()
s1 = input("Enter 1st string.  -->  ")
s2 = input("Enter 2nd string.  -->  ")
print()

if s1.upper() < s2.upper():
   print(s1,"goes alphabetically before",s2)
elif s1.upper() > s2.upper():
   print(s1,"goes alphabetically after",s2)   
else:
   print("Both strings are equal")   
 