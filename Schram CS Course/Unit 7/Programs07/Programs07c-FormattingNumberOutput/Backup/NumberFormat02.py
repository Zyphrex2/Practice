# NumberFormat02.py
# This program demonstrates one way to properly line
# numbers up by place value using the <format> command.  
# The 05 inside "{:05}" means each number will have 
# enough 0s placed at the front of the number to force
# it to be displayed as a 5 digit number.


print()
print("{:05}".format(1))
print("{:05}".format(12))
print("{:05}".format(123))
print("{:05}".format(1234))
print("{:05}".format(12345))


