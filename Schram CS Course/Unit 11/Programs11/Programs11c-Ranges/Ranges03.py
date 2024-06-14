# Ranges03.py
# This program defines several different ranges 
# using an <if..elif..else> structure.


print()
gpa = eval(input("What is your GPA?  -->  "))
print()

if gpa >= 3.9:
   print("Summa Cum Laude")
elif gpa >= 3.75:
   print("Magna Cum Laude")
elif gpa >= 3.5:
   print("Cum Laude")
elif gpa >= 2.65:
   print("Graduate without Honors")
else:
   print("Did not graduate")  
      