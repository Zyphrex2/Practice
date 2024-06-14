# ArrayCommands12.py
# This program was originally program InputProtection04.py from
# Chapter 11.  The second <while> loop shows that an array can  
# be used to make a long compound condition less complicated.
# Without it, the command would read:
# genderOK = gender=='M' or gender=='m' or gender=='F' or gender=='f'


sat = 0
satOK = False
while not satOK:
   sat = eval(input("\nEnter SAT  {400..1600}  -->  "))
   satOK = 400 <= sat <= 1600
   if not satOK:
      print("\nError! Please enter a number between 400 & 1600.")
   
gender = ''
genderOK = False
while not genderOK:
   gender = input("\nEnter your gender {M/F} -->  ")
   genderOK = gender in ['M','m','F','f'] # This is an array.
   if not genderOK:
      print("\nError! Please enter either an 'M' or an 'F'.")

lastName = input("\nEnter your last name    -->  ")
print()

if gender == 'M' or gender == 'm':
   print("Mr.",lastName,end = ", ")
if gender == 'F' or gender == 'f':
   print("Ms.",lastName,end = ", ")  
   
if sat >= 1100:
   print("you are admitted!")
else:
   print("you are not admitted.")    
        