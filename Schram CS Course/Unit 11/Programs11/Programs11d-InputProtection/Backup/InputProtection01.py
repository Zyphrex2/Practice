# InputProtection01.py
# This program enters the SAT score, gender and last name
# of a college applicant.  Nothing prevents the user from 
# entering invalid information for <sat> and <gender>.


print()
sat = eval(input("Enter SAT  {400..1600}  -->  "))
gender  =  input("Enter your gender {M/F} -->  ")
lastName = input("Enter your last name    -->  ")
print()

if gender == 'M' or gender == 'm':
   print("Mr.",lastName,end = ", ")
if gender == 'F' or gender == 'f':
   print("Ms.",lastName,end = ", ")  
   
if sat >= 1100:
   print("you are admitted!")
else:
   print("you are not admitted.")    
        