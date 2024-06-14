# StringCommands19.py
# This program demonstrates <isdecimal>, <isalpha>, <isalnum>
# and <isidentifier>.


s = "Exposure Computer Science 2020 in Python for CS1 & CS1-Honors"
print("\n" + s)
print(s.isdecimal(), s.isalpha(), s.isalnum(), s.isidentifier())

s = "ExposureComputerScience"
print("\n" + s)
print(s.isdecimal(), s.isalpha(), s.isalnum(), s.isidentifier())

s = "1996"
print("\n" + s)
print(s.isdecimal(), s.isalpha(), s.isalnum(), s.isidentifier())

s = "3.14159"
print("\n" + s)
print(s.isdecimal(), s.isalpha(), s.isalnum(), s.isidentifier())

s = "11A2B" 
print("\n" + s)
print(s.isdecimal(), s.isalpha(), s.isalnum(), s.isidentifier())

s = "A_108" 
print("\n" + s)
print(s.isdecimal(), s.isalpha(), s.isalnum(), s.isidentifier())
