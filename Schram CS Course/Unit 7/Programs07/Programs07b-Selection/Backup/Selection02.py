# Selection02.py
# This program demonstrates the Syntax Error
# you receive when you do not properly indent
# the programming statement(s) being controlled
# by a control structure.

# NOTE: In most languages, indentation is recommended.
#       In Python, indentation is required.


print()
sales = eval(input("Enter Sales  -->  "))
bonus = 0

if sales >= 500000:
bonus = 1000
   
print()
print("Christmas bonus:",bonus)   
