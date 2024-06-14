# KeyboardInput03.py
# This program enters 3 different names: <firstName>,
# <middleName> and <lastName>; on 3 different lines 
# and then combines them all into a full name.
# NOTE: You will not see the second prompt until you 
# finish entering the information from the first and 
# press <enter>.


print()

firstName  = input("Please enter your first name.   -->  ")
middleName = input("Please enter your middle name.  -->  ")
lastName   = input("Please enter your last name.    -->  ")

fullName = firstName + " " + middleName + " " + lastName

print()
print("Your full name is",fullName)
