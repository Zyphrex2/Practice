# StringCommands18.py
# This program demonstrates <capitalize>, <title>, 
# <islower>, <isupper> and <istitle>.
# Note that <capitalize> is not the same thing as <upper>.


s = "exposure computer science 2020 in python for CS1 & CS1-honors"
print("\n" + s)
print(s.islower(), s.isupper() ,s.istitle())

s = s.capitalize()
print("\n" + s)
print(s.islower(), s.isupper() ,s.istitle())

s = s.upper()
print("\n" + s)
print(s.islower(), s.isupper() ,s.istitle())

s = s.lower()
print("\n" + s)
print(s.islower(), s.isupper() ,s.istitle())

s = s.title()
print("\n" + s)
print(s.islower(), s.isupper() ,s.istitle())