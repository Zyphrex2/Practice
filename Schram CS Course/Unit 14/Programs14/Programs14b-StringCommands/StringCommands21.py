# StringCommands21.py
# This program demonstrates <isspace> and <isprintable>.


s = "Exposure Computer Science 2020 in Python for CS1 & CS1-Honors"
print("\n" + s)
print(s.isspace(), s.isprintable())

s = " "
print("\nSpace")
print(s.isspace(), s.isprintable())

s = ""
print("\nEmpty String")
print(s.isspace(), s.isprintable())

s = "\t"
print("\nTab Escape Sequence")
print(s.isspace(), s.isprintable())

s = "\n"
print("\nNew Line Escape Sequences")
print(s.isspace(), s.isprintable())
