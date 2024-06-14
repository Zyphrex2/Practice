# Nested06.py
# This program demonstrates that control structures
# can be nested with more than 2 levels.  
# This program is actually the entire previous 
# program nested inside a loop that repeats 5 times.
# NOTE: As you have more and more levels of nesting
#       indentation becomes more and more important.
# ALSO: This program does have an issue in that it
#       basically assumes you will always interview
#       exactly 5 students.


for k in range(5):
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
      
   print("\n------------------------------------")
  