# LastWord01.py
# This program will count backwards from 20 to 0.
# For each number, it will display whether it has
# 1 or 2 digits. Compare this Python code to the 
# code from other languages.


print()
for k in range (20, -1, -1): 
    if k >= 10:
        print (k,"is a 2-digit number.")
    else:
    	  print (k,"is a 1-digit number.")
        