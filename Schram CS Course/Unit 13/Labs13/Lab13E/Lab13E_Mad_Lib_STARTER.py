# Program:  Lab 13E Mad Lib
# Purpose:  Random selection of array elements

from random import *

heroList = ["Slope Dude", "Oatmeal Man", "Zippity Zoop"]
destinationList = ["Moon", "beach", "library"]
actionList = ["save humanity", "work on algebra problems", "juggle"]
vehicleList = ["sports car", "yacht", "fishing boat", "private jet"]
snackList = ["cheese puffs", "potato chips", "fruit"]
villainList = ["the Joker", "aliens", "angry robots"]


story = ""

story = "One day, my super hero friend "
randomIndex = randint(0, len(heroList) - 1)
superHero = heroList[randomIndex]
story += superHero

story += " and I went to the "
randomIndex = randint(0, len(destinationList) - 1)
destination = destinationList[randomIndex]
story += destination

story += " to "
randomIndex = randint(0, len(actionList) - 1)
action = actionList[randomIndex]
story += action

story += " while riding in a "
randomIndex = randint(0, len(vehicleList) - 1)
vehicle = vehicleList[randomIndex]
story += vehicle

story += " and eating "
randomIndex = randint(0, len(snackList) - 1)
snack = snackList[randomIndex]
story += snack

story += " while fighting "
randomIndex = randint(0, len(villainList) - 1)
villain = villainList[randomIndex]
story += villain
story += "."

story += "\n"  # this will create a new line


print("My Mad Lib Adventure Story")
print(story)