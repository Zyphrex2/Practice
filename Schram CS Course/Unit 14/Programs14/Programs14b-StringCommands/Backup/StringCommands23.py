# StringCommands23.py
# This program demonstrates how to use the <join> which is
# essentially the opposite of <split>.


words = ["The","quick","brown","fox","jumps","over","the","lazy","dogs."]

space = " "
sentence = space.join(words)
print()
print(sentence)

sentence = ",".join(words)
print()
print(sentence)

sentence = "<~>".join(words)
print()
print(sentence)

sentence = "".join(words)
print()
print(sentence)