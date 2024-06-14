# RandomNumbers03.py
# This program INCORRECTLY simulates rolling 
# dice 1,000,000 times.


from random import randint

sevens = 0
elevens = 0
snakeEyes = 0
doubles = 0

for roll in range(1000000):
   dice = randint(2,12)
   #
   if dice == 2:
      snakeEyes += 1
   #   
   if dice == 7:
      sevens += 1
   #   
   if dice == 11:
      elevens += 1

print()
print("# of Sevens:    ",sevens)
print("# of Elevens:   ",elevens)
print("# of Snake Eyes:",snakeEyes)
print("# of Doubles:   ",doubles)
