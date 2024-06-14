# MoreErrors04.py
# Fixing the Address Issue
# By Type Casting the <houseNumber> as a string,
# the computer is able to concatenate it to the 
# <streetName> to complete the <streetAddress>.


houseNumber = 811
streetName = " Fleming Trail"
streetAddress = str(houseNumber) + streetName

print()
print(streetAddress)

