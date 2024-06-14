# StringErrors04.py
# This program is supposed to CAPITALIZE all of the letters 
# in string <s> and then replace every 'A' with 'U'; however, 
# nothing happens. This Logic Error occurs when students 
# forget that the string commands do NOT alter the original 
# string at all.  Instead, they create an altered copy of 
# the string -- which this program does not use.


s = "banana"
print()
print(s)
s.upper()
print(s)
s.replace('A','U')
print(s)
