# Selection08.py
# This program shows a better way to do "Multi-Way 
# Selection" using <if..elif..else>.  The <elif> 
# command essentially combines the <else> with the 
# next <if>.  Not only is this less code to type, 
# it also has nicer indentation."


print()
grade = eval(input("Enter Number Grade  -->  "))
print()

if grade >= 90:
   print("You earned an A!")
elif grade >= 80:
   print("You earned a B.")
elif grade >= 70:
   print("You earned a C.")  
elif grade >= 60:
   print("You earned a D.")  
else:
   print("You earned an F.")     
                         
