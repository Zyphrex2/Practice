# LogicError03.py
# This program is also similar to program InputProtection03.py,
# but now there are 2 logic errors because DeMorgan's Law was 
# not followed when the <not> was distributed in the <while> 
# statements.  The result is the first loop will never execute,
# and the second loop will repeat forever.


print()

sat = 0
while sat < 400 and sat > 1600:
   sat = eval(input("Enter SAT  {400..1600}  -->  "))
   
gender = ''
while gender != 'M' or gender != 'F':
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
    