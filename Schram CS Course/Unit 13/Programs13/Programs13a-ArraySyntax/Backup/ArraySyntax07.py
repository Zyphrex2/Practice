# ArraySyntax07.py
# This program demonstrates a common mistake when 
# an array is traversed with a loop.  With 10 items 
# in the array, the indexes range from 0 to 9, but 
# the <while> loop erroneously counts from 1 to 10.  
# This also causes a "list index out of range" error.


list = [100,101,102,103,104,105,106,107,108,109]

print()
k = 1
while k <= 10:
   print(list[k])
   k += 1
 