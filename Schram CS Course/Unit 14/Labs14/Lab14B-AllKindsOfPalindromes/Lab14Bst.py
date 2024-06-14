# Lab14Bst.py
# "All Kinds Of Palindromes"
# This is the student, starting version of Lab 14B.
# NOTE: This lab is meant for students in CS1-HONORS.
#       Students in REGULAR CS1 will do Lab 14A.


def heading():
   print()
   print("********************************************")
   print("Lab 14B, All Kinds Of Palindromes")
   print("80 Point Version")
   print("By: DAVID BARDAN") # Substitute your own name here.
   print("********************************************")


def isPal(text):
   text = text.lower()
   reversetext = ""
   for i in range(len(text) - 1, -1, -1):
      reversetext += text[i]
   return text == reversetext
   

def purge(text):
   text = text.lower()
   newtext = ""
   letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','h','j','k','l','z','x','c','v','b','n','m']
   for char in text:
      if char in letters:
         newtext += char
   return newtext

def recursivePalCheck(text, numberOfLetters):

   numberOfLetters += 1
   emptyReverse = ""
   empty = ""

   length = len(text)-1

   for i in range(length, length - numberOfLetters, -1):
      emptyReverse += text[i]
   
   for i in range(len(emptyReverse)-1, -1, -1):
      empty += emptyReverse[i]
   

   if empty == emptyReverse:
      return numberOfLetters
   else:
      return recursivePalCheck(text, numberOfLetters)

def leastPal(text):
   
   reversetext = ""

   for i in range(len(text) - 1, -1, -1):
      reversetext += text[i]

   numLetters = recursivePalCheck(text, 1)

   leastPalindrome = ""
   reversetext = reversetext[numLetters:]
   leastPalindrome = text + reversetext

   return leastPalindrome
  
      
   
##########
#  MAIN  #
##########

heading() 
finished = False
while not finished:
   print("\n") 
   text = input("Enter a string  -->  ")
   print("\nPalindrome:        ",isPal(text))
   print("Almost Palindrome: ",isPal(purge(text)))
   print("Least Palindrome:  ",leastPal(text))
   choice = input("\nDo you wish to repeat this program? {Y/N} --> ")
   if choice.upper()[0] != 'Y':
      finished = True
   