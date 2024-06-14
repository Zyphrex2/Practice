# RandomArrays02.py
# This program will display 15 random sentences.
# With 7 different ranks, 7 different people, 
# 7 different actions and 7 different locations,
# there are more than 2400 different sentences possible.


from random import randint


ranks = ["Private","Corporal","Sargent","Lieutenant","Captain","Major","General"]

names = ["Smith","Gonzales","Brown","Jackson","Powers","Jones","Nguyen"]

actions = ["drive the tank","drive the jeep","take the troops",
           "bring all supplies","escort the visitor","prepare to relocate",
           "bring the Admiral"]

locations = ["over the next hill", "to the top of the mountain",
             "outside the barracks", "30 miles into the desert", 
             "to the middle of the forest", "to my present location", 
             "to anywhere but here"]


for k in range(15):
   randomRank     = randint(0,len(ranks)-1)
   randomPerson   = randint(0,len(names)-1)
   randomAction   = randint(0,len(actions)-1)
   randomLocation = randint(0,len(locations)-1)
   
   sentence = ranks[randomRank] + " " + names[randomPerson] + ", " + \
              actions[randomAction] + " " + locations[randomLocation] + "."
   
   print("\n" + sentence)
   