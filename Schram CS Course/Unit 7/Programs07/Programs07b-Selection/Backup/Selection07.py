# Selection07.py
# This program fixes the Logic Error of the 
# previous program by adding several strategic 
# <else> statements which will ensure that only 
# 1 letter grade is displayed.  While this works, 
# the program's indentation is somewhat annoying.


print()
grade = eval(input("Enter Number Grade  -->  "))
print()

if grade >= 90:
   print("You earned an A!")
else:
   if grade >= 80:
      print("You earned a B.")
   else:
      if grade >= 70:
         print("You earned a C.")  
      else:   
         if grade >= 60:
            print("You earned a D.")  
         else:
            print("You earned an F.")  
                 