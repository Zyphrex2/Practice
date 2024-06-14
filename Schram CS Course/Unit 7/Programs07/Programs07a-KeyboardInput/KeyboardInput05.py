# KeyboardInput05.py
# This program demonstrates the proper way to enter
# numerical input by using the <eval> function.
# The function makes the computer EVALuate the 
# input to see what kind of information it is
# and properly identify numerical input.


print()

num1 = eval(input("Please enter the 1st number.  -->  "))
num2 = eval(input("Please enter the 2nd number.  -->  "))

sum = num1 + num2

print()
print("The sum of",num1,"and",num2,"is",sum)
