# Nested05.py
# This program repeats Selection12.py from Chapter 7.
# It is another example of "Nested Control Structures",
# in this case, "Nested Selection".


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
