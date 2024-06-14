# StringCommands22.py
# This program demonstrates how to use the <split> command to
# "split" a something like a sentence into an array of words.


title = "Exposure Computer Science 2020 for CS1 & CS1-Honors"
words = title.split()
print()
print(words)

title = "Exposure, Computer, Science, 2020, for, CS1, &, CS1-Honors"
words = title.split()
print()
print(words)

title = "Exposure, Computer, Science, 2020, for, CS1, &, CS1-Honors"
words = title.split(',')
print()
print(words)  

title = "Exposure, Computer, Science, 2020, for, CS1, &, CS1-Honors"
words = title.split(', ')
print()
print(words) 

title = "Exposure Computer Science 2020 for CS1 & CS1-Honors"
words = title.split('&')
print()
print(words)

title = "Exposure Computer Science 2020 for CS1 & CS1-Honors"
words = title.split('%')
print()
print(words)
