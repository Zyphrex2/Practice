# Selection01.py
# This program demonstrates one-way selection
# with <if>.  Run the program twice.  
# First with <sales> equal to 300,000 and a 
# second time with <sales> equal to 500,000.


print()
sales = eval(input("Enter Sales  -->  "))
bonus = 0

if sales >= 500000:
   bonus = 1000
   
print()
print("Christmas bonus:",bonus)   
