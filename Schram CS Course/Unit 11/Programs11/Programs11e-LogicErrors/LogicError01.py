# LogicError01.py
# This program is similar to program InputProtection02.py, 
# but now there are 2 logic errors because the parentheses
# in the <while> statements do not contain the entire Boolean 
# expression.  This means the <not> only applies to the first 
# part of the expression.  When you run the program it may 
# seem to work, unless you are female or enter an SAT score 
# above 1600.


print()

sat = 0
while not(sat >= 400) and sat <= 1600:
   sat = eval(input("Enter SAT  {400..1600}  -->  "))
   
gender = ''
while not(gender == 'M') or gender == 'F':
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
    