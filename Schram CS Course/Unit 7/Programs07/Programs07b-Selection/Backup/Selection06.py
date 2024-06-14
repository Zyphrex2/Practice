# Selection06.py
# This program is supposed to display the letter grade
# earned based on the number grade entered by the user.
# Since there are more than 2 possible paths (A,B,C,D,F)
# this would be an example of "Multi-Way Selection" if
# the program worked.  Using 5 separate <if> statements
# has created a Logic Error that gives strange output.


print()
grade = eval(input("Enter Number Grade  -->  "))
print()

if grade >= 90:
   print("You earned an A!")
if grade >= 80:
   print("You earned a B.")
if grade >= 70:
   print("You earned a C.")  
if grade >= 60:
   print("You earned a D.")     
if grade >= 0:
   print("You earned an F.")   
      
       
