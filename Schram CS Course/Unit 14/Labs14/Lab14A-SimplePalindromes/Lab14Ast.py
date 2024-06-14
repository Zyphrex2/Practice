# Lab14Ast.py
# The "Simple Palindromes" Program
# This is the student, starting version of Lab 14A.
# Students need to complete the <isPal> function.
# NOTE: This lab is meant for students in REGULAR CS1.
#       Students in CS1-HONORS will do Lab 14B.


def heading():
   print()
   print("********************************************")
   print("Lab 14A, Simple Palindromes")
   print("90 Point Version")
   print("By: DAVID BARDAN") # Substitute your own name here.
   print("********************************************")


def isPal(text):
   text = text.upper()
   reversetext = ""
   for i in range(len(text) - 1, -1, -1):
      reversetext += text[i]
   return text == reversetext
   




   
##########
#  MAIN  #
##########

heading() 
finished = False
while not finished:
   print("\n") 
   text = input("Enter a string  -->  ")
   print("\nPalindrome:        ",isPal(text))
   choice = input("\nDo you wish to repeat this program? {Y/N} --> ")
   if choice.upper()[0] != 'Y':
      finished = True
   