# Nested08.py
# This program fixes the issue of the previous program.
# Now everything is inside a <while> loop.
# At the conclusion of each interview the user has
# the option to repeat the program.  
# The <while> loop makes the program repeat as long
# as the user responds with a capital 'Y'.


response = 'Y';

while response == 'Y':  # Note: Only capital 'Y' will make the loop repeat.
   print()
   sat = eval(input("Enter SAT score  -->  "))
   print()
   
   if sat >= 1100:
      print("You are admitted.")
      print("Orientation will start in June.")
      print()
      income = eval(input("Enter your family income  -->  "))
      print()
      if income < 20000:
         print("You qualify for financial aid.")
      else:
         print("You do not qualify for financial aid.") 
   else:
      print("You are not admitted.")
      print("Please try again when your SAT improves.")
      
   print()
   response = input("Do you want to interview another student?  {Y/N}  -->  ")
     