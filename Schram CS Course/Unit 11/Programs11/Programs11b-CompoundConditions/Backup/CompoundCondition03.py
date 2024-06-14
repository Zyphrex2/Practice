# CompoundCondition03.py
# This program demonstrates the logical <not> operator.
# NOTE: This also requires (parentheses).


print()
education  = eval(input("Enter years of education   -->  "))
experience = eval(input("Enter years of experience  -->  "))
print()

if not(education >= 16 or experience >= 5):
   print("You are hired!")
else:
   print("You are not qualified.")
  