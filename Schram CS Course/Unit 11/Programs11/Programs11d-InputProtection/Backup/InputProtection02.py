# InputProtection02.py
# This program improves on the previous program by 
# adding 2 <while> loops that will force the user to 
# keep re-entering the information until it is valid.


print()

sat = 0
while not(sat >= 400 and sat <= 1600):
   sat = eval(input("Enter SAT  {400..1600}  -->  "))
   
gender = ''
while not(gender == 'M' or gender == 'F'): 
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
        