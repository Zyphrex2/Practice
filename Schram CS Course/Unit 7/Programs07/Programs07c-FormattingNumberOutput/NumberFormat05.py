# NumberFormat05.py
# This program demonstrates how to add commas (,)
# as a "thousand separator".  It may seem like
# it stops working at 10 million.  The problem is
# the commas count as digits.


print()
print("{:9,}".format(1))
print("{:9,}".format(12))
print("{:9,}".format(123))
print("{:9,}".format(1234))
print("{:9,}".format(12345))
print("{:9,}".format(123456))
print("{:9,}".format(1234567))
print("{:9,}".format(12345678))
print("{:9,}".format(123456789))

