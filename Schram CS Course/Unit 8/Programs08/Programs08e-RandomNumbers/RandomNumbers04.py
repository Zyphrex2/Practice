# RandomNumbers04.py
# This program PROPERLY simulates rolling 
# dice 1,000,000 times.


from random import randint

sevens = 0
elevens = 0
snakeEyes = 0
doubles = 0

for roll in range(1000000):
   die1 = randint(1,6)
   die2 = randint(1,6)
   diceTotal = die1 + die2
   #
   if diceTotal == 2:
      snakeEyes += 1
   if diceTotal == 7:
      sevens += 1
   if diceTotal == 11:
      elevens += 1
   if die1 == die2:
      doubles += 1   

print()
print("# of Sevens:    ",sevens)
print("# of Elevens:   ",elevens)
print("# of Snake Eyes:",snakeEyes)
print("# of Doubles:   ",doubles)
