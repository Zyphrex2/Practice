# SwappingValues04.py
# Swapping the values of 2 string variables
# You can swap other data types as well.
# NOTE: If you swap 2 variables twice, they
# wind up with their original values.


print()
name1 = "Tom"
name2 = "Sue"
print(name1,name2)

# first swap
temp = name1
name1 = name2
name2 = temp
print(name1,name2)

# second swap
name1,name2 = name2,name1
print(name1,name2)
