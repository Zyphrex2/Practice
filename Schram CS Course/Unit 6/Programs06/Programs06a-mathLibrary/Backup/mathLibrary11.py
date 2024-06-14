# mathLibrary11.py
# When the fractional value is exactly .5, the 
# <round> function does not behave as expected.
# This is because Python's <round> function uses
# "banker's rounding" a.k.a. "round-to-even".


from math import *

print()
print("0.5 rounded to the nearest even# is",round(0.5))
print("1.5 rounded to the nearest even# is",round(1.5))
print("2.5 rounded to the nearest even# is",round(2.5))
print("3.5 rounded to the nearest even# is",round(3.5))
print("4.5 rounded to the nearest even# is",round(4.5))
print("5.5 rounded to the nearest even# is",round(5.5))
print("6.5 rounded to the nearest even# is",round(6.5))
print("7.5 rounded to the nearest even# is",round(7.5))
print("8.5 rounded to the nearest even# is",round(8.5))
print("9.5 rounded to the nearest even# is",round(9.5))
