# Selection03.py
# This program demonstrates a control structure
# can control multiple programming commands as 
# long as proper, consistent indentation is used.


print()
sales = eval(input("Enter Sales  -->  "))
bonus = 0

if sales >= 500000:
   print("\nCONGRATULATIONS!")
   print("You sold half a million dollars in merchandise!")
   print("You will receive a $1000 Christmas Bonus!")
   print("Keep up the good work!")
   bonus = 1000
   
print()
print("Christmas bonus:",bonus)   
