# Boolean05.py
# This program executes in the same manner as Boolean04.py.  
# The abbreviated Boolean assignment statement is used in 
# place of the longer <if...else> expression.



gcf = 0
attempt = 0
correct = False

while not correct:
   attempt += 1
   gcf = eval(input("\nWhat is the GCF of 120 and 108?  -->  "))
   correct = gcf == 12
   
if attempt == 1:
   print("\nYou got it on the first try!")
else:
   print("\nYou answered it correctly after",attempt,"attempts.")   