# Repetition08.py
# This program is supposed to keep repeating until 
# a correct PIN of 5678 is entered.
# The program does not work because the <for> 
# loop is used at a time that is not appropriate.
# The <for> loop is meant for "fixed" repetition.
# Entering a PIN is an example of "conditional" repetition.


for k in range(10):
   print()
   pin = input("Enter 4 digit PIN#.  -->  ")
   if pin != "5678":
      print("\nThat is not the correct PIN.  Try Again.")

print("\nYou are now logged in.  Welcome to the program.")
