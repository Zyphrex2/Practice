x = 0
y = 0
correctX = 5
correctY = 5
coords = [x,y]
correctCoords = [correctX, correctY]
while coords != correctCoords:
   userInput = input("W, A, S, or D: ")
   if userInput == "W" or userInput == "w":
      y += 1
   elif userInput == "A" or userInput == "a":
      x += -1
   elif userInput == "S" or userInput == "s":
      y += -1
   elif userInput == "D" or userInput == "d":
      x += 1
   else:
      print("Invalid Input")
   coords = [x,y]
   print(coords)
print("Congratulations!")