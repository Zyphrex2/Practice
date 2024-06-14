# Repetition09.py
# This program fixes the problem of the previous program 
# by using a <while> loop.  Now the loop will stop when 
# the correct PIN of 5678 is entered.


pin = ""
while pin != "5678":
   print()
   pin = input("Enter 4 digit PIN#.  -->  ")
   if pin != "5678":
      print("\nThat is not the correct PIN.  Try Again.")

print("\nYou are now logged in.  Welcome to the program.")
