# Lab14Cst.py
# "Number Systems - Part II"
# This is the student, starting version of Lab 14C.


def heading():
   print()
   print("********************************************")
   print("Lab 14C, Number Systems - Part II")
   print("80 Point Version")
   print("By: JOHN SMITH") # Substitute your own name here.
   print("********************************************")
   print("\n")
   

def bin2dec(bin):
   # precondition:  bin is a string storing an 8-bit sequence of 1s & 0s.
   # postcondition: The decimal equivalent of bin is returned.
   dec = 0

   for i in range(len(bin)):
      if bin[len(bin) - (i+1)] == 1:
         dec += 2 ** (len(bin) - i)

   return dec 
   
     
      
##########
#  MAIN  #
##########

heading()
print(bin2dec("11001000"))
print(bin2dec("01100100"))
print(bin2dec("00110010"))
print(bin2dec("00011001"))

# Required for the 110 Point Version Only:
#print(bin2dec("1000000001"))
#print(bin2dec("1101"))
#print(bin2dec("101"))
#print(bin2dec("11"))
#print(bin2dec("0"))
#print(bin2dec("1100100000000"))
                 
   