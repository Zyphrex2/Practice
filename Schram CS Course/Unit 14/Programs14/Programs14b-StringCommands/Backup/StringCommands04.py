# StringCommands04.py
# This program demonstrates how to take 
# one string and create a second string
# that is a reverse of the first.


s1 = "Madam I'm Adam"
s2 = ""
n = len(s1)

# Count from the last index (n-1)
# to the first index (0) backwards.
for k in range(n-1,-1,-1):
   s2 += s1[k]

print()
print(s1)
print(s2)
