# KeyboardInput06.py
# This program computes the average of 3 numbers
# entered by the user.  Note that this works for 
# both integers and real numbers.


print()

num1 = eval(input("Please enter the 1st number.  -->  "))
num2 = eval(input("Please enter the 2nd number.  -->  "))
num3 = eval(input("Please enter the 3rd number.  -->  "))

average = (num1 + num2 + num3) / 3

print()
print("The average of",num1,"and",num2,"and",num3,"is",average)
