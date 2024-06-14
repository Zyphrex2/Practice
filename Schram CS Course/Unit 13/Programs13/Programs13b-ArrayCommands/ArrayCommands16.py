# ArrayCommands16.py   
# This program shows that <del> allows you to delete
# an entire "slice" from an array.  Remember, you need 
# to specify the starting and stopping index.  In this 
# program, the [2:5] specifies deleting the names from 
# indexes 2-4 (not 5).  This cannot be done with <pop>.


names = ["John","Greg","Maria","Heidi","Mike","Kisha","Diana","David"]

print()
print(names)

del names[2:5]

print()
print(names)
