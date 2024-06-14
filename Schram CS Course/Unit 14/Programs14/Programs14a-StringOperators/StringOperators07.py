# StringOperators07.py
# This program demonstrates that the "greater than" > and
# less than < operators can compare strings alphabetically.
# NOTE: This program will not work properly if one string 
# starts with a CAPITAL letter and the other string does not.
# A later program example will fix this.


print()
s1 = input("Enter 1st string.  -->  ")
s2 = input("Enter 2nd string.  -->  ")
print()

if s1 < s2:
   print(s1,"goes alphabetically before",s2)
elif s1 > s2:
   print(s1,"goes alphabetically after",s2)   
else:
   print("Both strings are equal")   

