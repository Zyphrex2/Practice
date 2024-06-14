# Selection11.py
# This program has 2 separate <if..else> structures.
# The first determines if a student is admitted to
# the college based on his/her SAT score.
# The second determines is that student qualifies
# for financial aid based on his/her family income.
# The problem with this program is that even if the
# student is not admitted, it still asks about
# family income and has the potential of telling 
# a student who was not admitted that he/she 
# qualifies for financial aid.


print()
sat = eval(input("Enter SAT score --> "))
print()

if sat >= 1100:
   print("You are admitted.")
   print("Orientation will start in June.")
else:
   print("You are not admitted.")
   print("Please try again when your SAT improves.")
   
   
print()   
income = eval(input("Enter your family income --> "))
print()

if income < 20000:
   print("You qualify for financial aid.")
else:
   print("You do not qualify for financial aid.")   
   