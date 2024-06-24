#hangman game
from random import *

wordList =  ('sleep', 'longer', 'believe', 'morning', 'check')
word = wordList[randint(0, 4)] # Choosing a random word from list
guessesSoFar = []
guess = ''
for letter in word:
    guess += '_'
guessCount = 0
while guess != word:
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
    if guessCount > 5:
        print('Sorry! Out of guesses. The word was ' + word)
        exit()
print('Congratulations! You won! The word was: ' + guess)