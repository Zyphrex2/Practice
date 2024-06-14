# Boolean04.py
# This program demonstrates a practical use of the <bool> 
# data type, which only has two values, <True> and <False>.   
# NOTE: Boolean variables add readability to programs.


gcf = 0
attempt = 0
correct = False

while not correct:
   attempt += 1
   gcf = eval(input("\nWhat is the GCF of 120 and 108?  -->  "))
   if gcf == 12:
      correct = True
   else:
      correct = False   
   
if attempt == 1:
   print("\nYou got it on the first try!")
else:
   print("\nYou answered it correctly after",attempt,"attempts.")  
    