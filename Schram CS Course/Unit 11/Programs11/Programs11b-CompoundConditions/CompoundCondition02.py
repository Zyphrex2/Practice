# CompoundCondition02.py
# This program demonstrates compound decisions 
# with the logical <and> operator.


print()
education  = eval(input("Enter years of education   -->  "))
experience = eval(input("Enter years of experience  -->  "))
print()

if education >= 16 and experience >= 5:
   print("You are hired!")
else:
   print("You are not qualified.")
  
  