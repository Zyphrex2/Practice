# Functions02.py
# This example returns a Boolean value, which is used
# frequently to check for correct user keyboard input.
# NOTE: This program also demonstrates the true purpose of
# Boolean variables.  They make the program more readable.


def checkPIN(pin):
   if pin == 1234:
      return True
   else:
      return False   
   
   

##########
#  MAIN  #
##########

correctPIN = False
while(not correctPIN):
   pin = eval(input("\nEnter your 4 digit PIN  -->  "))
   correctPIN = checkPIN(pin)
   if not correctPIN:
      print("\nIncorrect PIN.  Please try again.")

print("\nYou have successfully logged in.")
print("Select your bank transaction:")
