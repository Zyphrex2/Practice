# StringCommands06.py
# This program demonstrates the <find> and "Reverse Find" <rfind> commands.
# <find> returns the index of the first occurrence of the substring parameter. 
# <rfind> returns the index of the last occurrence of the substring parameter. 
# Both return -1 if the substring parameter is not found in the original string.


s1 = "racecar"
s2 = "racecar in the car port"
s3 = "car"

index1 = s1.find(s3)
index2 = s1.rfind(s3)
index3 = s2.find(s3)
index4 = s2.rfind(s3)
index5 = s3.find("qwerty")
index6 = s3.rfind("qwerty")

print()
print("The first occurrence of",s3,"in",s1,"is at index",index1)
print("and the last occurrence is at index",index2)

print()
print("The first occurrence of",s3,"in",s2,"is at index",index3)
print("and the last occurrence is at index",index4)

print()
print("The first occurrence of qwerty in",s3,"is at index",index5)
print("and the last occurrence is at index",index6)
