# LogicError02.py
# This program is similar to program InputProtection03.py,
# but now there is a subtle logic error in the first loop.
# The opposite is sat >=  400 is sat <  400, NOT sat <=  400.
# The opposite is sat <= 1600 is sat > 1600, NOT sat >= 1600.
# While the program works most of the time, it will not work
# for the "border cases" when the SAT is exactly 400 or 1600.


print()

sat = 0
while sat <= 400 or sat >= 1600:
   sat = eval(input("Enter SAT  {400..1600}  -->  "))
   
gender = ''
while gender != 'M' and gender != 'F':
   gender = input("Enter your gender {M/F} -->  ")

lastName = input("Enter your last name    -->  ")
print()

if gender == 'M':
   print("Mr.",lastName,end = ", ")
if gender == 'F':
   print("Ms.",lastName,end = ", ")  
   
if sat >= 1100:
   print("you are admitted!")
else:
   print("you are not admitted.")     
       