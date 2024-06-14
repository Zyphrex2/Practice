# ArrayCommands20.py
# This program demonstrates a problem that happens when you try
# to sort strings that contain both CAPITAL and lowercase letters.
# Capital letters have numeric code values from 65-90.
# Lowercase letters have numeric code values from 97-122.  
# If lowercase letters are sorted together with capital letters,
# the capitals will come first because of the smaller code values.


animals = ["hipo","monkey","ZEBRA","TOUCAN","lion","GIRAFFE","cheetah","ELEPHANT"]       

print()
print(sorted(animals))
animals.sort()
print(animals)
 