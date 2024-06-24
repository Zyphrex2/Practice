#hangman game
from random import *

wordList =  ('sleep', 'longer', 'believe', 'morning', 'check')
word = wordList[randint(0, 4)] # Choosing a random word from list

#init variables

guess = ''
for letter in word:
    guess += '_'

guessCount = 0

#guessing loop

while guess != word:
    #reset vars
    k = 0
    wasInWord = False

    print('Guesses Left: ' + str(6 - guessCount))
    print('So far, you have: \n' + guess)

    char = input("Please input a character: ")
    while len(char) != 1:
        len = input("Sorry, guesses are one character long: ")
    
    for i in word:
        k += 1
        if char == i:
            guess = guess[0:k-1] + char + guess[k:]
            wasInWord = True
    
    if wasInWord == False:
        guessCount += 1
    
    #if you lose:
    if guessCount > 5:
        print('Sorry! Out of guesses. The word was ' + word)
        exit()

#if you win and break loop:
print('Congratulations! You won! The word was: ' + guess)