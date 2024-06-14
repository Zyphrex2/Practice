# StringCommands20.py
# This program demonstrates how <isdigit> and 
# <isnumeric> are different from <isdecimal>.
# NOTE: This program will not execute in jGRASP.
# You will need to use the Python Shell.

s = "10" 
print(s.isdecimal(), s.isdigit(), s.isnumeric())

s = "10���" 
print(s.isdecimal(), s.isdigit(), s.isnumeric())

s = "10������" 
print(s.isdecimal(), s.isdigit(), s.isnumeric())

s = "3.14159" 
print(s.isdecimal(), s.isdigit(), s.isnumeric())
