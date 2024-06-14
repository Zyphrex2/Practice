# Program Lab14D ASCII Tables
# Purpose:  Practice using the chr and ord functions
# to convert between ASCII codes and string characters.

# Procedure: generateAsciiTable
# Input:  String for which a table is generated
# Return:  None
def generateAsciiTable(stringInput):
   for i in stringInput:
      print(i, ord(i))
   print("ASCII Table Complete\n")


# Procedure: decodeAsciiCodeArray
# Purpose Given an array of ASCII code integers, call
# the chr function to find the associated character
# and print out the secret message.
# Input:  Array of integers, ASCII codes
# Return:  None
def decodeAsciiCodeArray(asciiArray):
   emptyStr = ""
   for i in asciiArray:
      emptyStr += chr(i)
   print("Decoded Message:", emptyStr)
   


############## MAIN PROGRAM ##############
   
# String of the lower case letters
# Do not create a string for the upper case alphabet   
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Lower Case Letters: Call procedure to print the ASCII table
print("ASCII Table: Lower Case Letters")
generateAsciiTable(alphabet)


# Upper Case Letters: Call procedure to print the ASCII table
print("ASCII Table: Upper Case Letters")
generateAsciiTable(alphabet.upper())


# Write and call the procedure decodeAsciiCodeArray
# to convert from ASCII code to characters to decode the
# secret message
secretMsg = [82, 97, 110, 103, 101, 114, 67, 83, 82, 85, 76, 69, 83]
decodeAsciiCodeArray(secretMsg)