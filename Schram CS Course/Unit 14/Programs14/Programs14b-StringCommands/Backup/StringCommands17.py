# StringCommands17.py
# This program fixes the issue of the previous program 
# by first checking if a character is a lowercase letter 
# before capitalizing it.


def allCAPS(strOld):
   strNew = ""
   for k in range(len(strOld)):
      if strOld[k] >= 'a' and strOld[k] <= 'z':
         ascii = ord(strOld[k])
         strNew += chr(ascii - 32)
      else:
         strNew += strOld[k]   
   return strNew   



##########
## MAIN ##
##########

title = "exposure computer science for CS1 & CS1-Honors"
newTitle = allCAPS(title)
print()
print(title) 
print(newTitle)   
   


