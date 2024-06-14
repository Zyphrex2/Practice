# Nested07.py
# This program is very similar to the previous
# program.  The different is that it begins with
# an input statement that allows the interviewer
# to enter the number of students that he/she
# needs to interview.


print()
numStudents = eval(input("How many students do you need to interview?  -->  "))

for k in range(numStudents):
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
  