# Selection12.py
# This program fixes the issue of the previous program 
# by "nesting" the second <if..else> structure inside
# the <if> part of the first.  Now, the "family income"
# question is only asked to students who are admitted.
# NOTE: Proper indentation is VERY important here.


print()
sat = eval(input("Enter SAT score --> "))
print()

if sat >= 1100:
   print("You are admitted.")
   print("Orientation will start in June.")
   print()
   income = eval(input("Enter your family income --> "))
   print()
   if income < 20000:
      print("You qualify for financial aid.")
   else:
      print("You do not qualify for financial aid.") 
else:
   print("You are not admitted.")
   print("Please try again when your SAT improves.")