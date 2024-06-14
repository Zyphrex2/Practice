# NumberFormat04.py
# This program demonstrates what happens when the
# format size for the number is not large enough.
# If the format is not possible, it is simply 
# ignored.  There is no error message.  


print()
print("{:5}".format(1))
print("{:5}".format(12))
print("{:5}".format(123))
print("{:5}".format(1234))
print("{:5}".format(12345))
print("{:5}".format(123456))
print("{:5}".format(1234567))
print("{:5}".format(12345678))
print("{:5}".format(123456789))

