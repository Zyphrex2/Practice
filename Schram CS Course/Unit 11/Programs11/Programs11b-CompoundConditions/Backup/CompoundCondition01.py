# CompoundCondition01.py
# This program demonstrates compound decisions 
# with the logical <or> operator.


print()
education  = eval(input("Enter years of education   -->  "))
experience = eval(input("Enter years of experience  -->  "))
print()

if education >= 16 or experience >= 5:
   print("You are hired!")
else:
   print("You are not qualified.")
  