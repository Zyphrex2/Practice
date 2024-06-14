# Boolean03.py
# This program shows a Boolean expression 
# being used in a <while> loop.


gcf = 0
attempt = 0

while gcf != 12:
   attempt += 1
   gcf = eval(input("\nWhat is the GCF of 120 and 108?  -->  "))
   
if attempt == 1:
   print("\nYou got it on the first try!")
else:
   print("\nYou answered it correctly after",attempt,"attempts.")   
   