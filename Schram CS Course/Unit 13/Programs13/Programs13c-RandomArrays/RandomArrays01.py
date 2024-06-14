# RandomArrays01.py
# This program fills an array with random 
# 3-digit integers and then displays the 
# entire contents of the array.


from random import randint


list = []
for k in range(20):
   list.append(randint(100,999))

print()
for k in range(20):
   print("list["+str(k)+"] =",list[k])
 