# Selection05.py
# This program demonstrates that multiple program 
# statements can be controlled in both parts of an 
# <if...else> structure as long as proper, consistent
# indentation is used.  Run the program twice:  
# First with 1100, then with 1099.


print()
sat = eval(input("Enter SAT score  -->  "))
print()

if sat >= 1100:
   print("You are admitted.")
   print("Orientation will start in June.")
else:
   print("You are not admitted.")
   print("Please try again when your SAT improves.")
   