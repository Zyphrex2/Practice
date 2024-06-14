# Selection09.py
# This program demonstrates a number of things:
# 1. Selection can be based on text values also, 
#    not just number values.
# 2. As with other selection structures, Multi-Way
#    Selection can control multiple programming 
#    commands as long as proper, consistent 
#    indentation is used.
# 3. The program will not work properly if the 
#    user does not enter an A, B, C, D or F.


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
   