# StringCommands16.py
# This program attempts to use <ord> and <chr> to convert 
# a string to all CAPITAL letters, like the <upper> command.
# The problem is it performs the conversion on all of the 
# characters, not just the lowercase letters.


def allCAPS(strOld):
   strNew = ""
   for k in range(len(strOld)):
      ascii = ord(strOld[k])
      strNew += chr(ascii - 32)
   return strNew   



##########
## MAIN ##
##########

title = "exposure computer science for CS1 & CS1-Honors"
newTitle = allCAPS(title)
print()
print(title) 
print(newTitle)   
   


