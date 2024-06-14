# Selection10.py
# This program demonstrates how the <else> command
# is used in Multi-Way Selection to deal with the
# case of a value that does not match any of the
# cases in your <if..elif> structure.


print()
grade = input("Enter Letter Grade  -->  ")
print()

if grade == 'A':
   print("You grade is 90 or above.")
   print("Excellent!")
elif grade == 'B':
   print("You grade is in the 80s.")
   print("Good")
elif grade == 'C':
   print("You grade is in the 70s.")
   print("Fair") 
elif grade == 'D':
   print("You grade is in the 60s.")
   print("Poor")  
elif grade == 'F':
   print("You grade is below 60.")  
   print("Bad") 
else:
   print("You did not enter an A, B, C, D or F.")  
   print("Please re-run the program and try again.")         