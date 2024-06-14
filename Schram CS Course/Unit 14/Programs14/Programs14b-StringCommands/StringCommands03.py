# StringCommands03.py
# This program demonstrates how to "traverse"
# a string using a <for> loop.  Note that this
# can be done both forwards and backwards.


s = "COMPUTER"
n = len(s)

print()
for k in range(n):
   print(s[k])
print()   

# Count from the last index (n-1)
# to the first index (0) backwards.
for k in range(n-1,-1,-1):
   print(s[k], end = "")
print()
