# SimpleProcedures06.py
# This program shows that in Python, 
# the "Procedure Definitions" must
# come before the "Procedure Calls".


###########################
#  MAIN: Procedure Calls  #  
########################### 

displayName()
displayStreetAddress()
displayCityStateZip()



###########################
#  Procedure Definitions  #  
########################### 

def displayName():
   print()
   print("Kathy Smith")


def displayStreetAddress():
   print("7003 Orleans Court")


def displayCityStateZip():
   print("Kensington, MD 20795")
