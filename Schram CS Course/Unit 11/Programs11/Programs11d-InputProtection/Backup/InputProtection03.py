# InputProtection03.py
# This program "distributes the not" in the  
# <while> loops using DeMorgan's Law.


print()

sat = 0
while sat < 400 or sat > 1600:
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