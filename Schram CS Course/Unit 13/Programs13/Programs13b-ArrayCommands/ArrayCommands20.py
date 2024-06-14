# ArrayCommands20.py
# This program demonstrates the <sorted> function.
# While similar to the <sort> command, there are 2
# important differences:
# 1. <sorted> does not actually sort the array.  
#    Instead, it returns a sorted copy of the array.
# 2. <sorted> has an option to sort in reverse order.


gpas1 = [3.9,2.75,2.1,1.65,4.0,3.25,2.45,0.95,3.88,3.75]       

gpas2 = sorted(gpas1)

gpas3 = sorted(gpas1, reverse=True)

print()
print(gpas3)
print(gpas2)
print(gpas1)
