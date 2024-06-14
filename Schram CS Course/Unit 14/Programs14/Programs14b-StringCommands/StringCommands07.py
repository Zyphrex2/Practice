# StringCommands07.py
# This program demonstrates the <count>,
# <startswith> and <endswith> commands.


s = "HOW MANY BANANAS ARE ON ANA'S BANANA BOAT"
print()
print(s.count("BANANA"))
print(s.count("AN"))
print(s.count("AN",9,29))
print(s.startswith("HOW"))
print(s.startswith("BANANA"))
print(s.endswith("BOAT"))
print(s.endswith("boat"))


