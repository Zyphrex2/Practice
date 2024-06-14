# Lab07Ast.pv
# "The Speeding Ticket Program"
# This is the student, starting version of Lab 07A.


print()
print("********************************************")
print("Lab 07A, The Speeding Ticket Program")
print("100 Point Version")
print("By: DAVID BARDAN") # Substitute your own name here.
print("********************************************")
print("\n")

speedDiff =  -(int(input("What is the posted speed limit?  -->  "))) + (int(input("\nHow fast was the car travelling in mph?  -->  ")))
ticketAmount = 75 + 6 * (speedDiff)
if speedDiff > 30: ticketAmount += 160
if input("\nDid the violation occur in a school zone?  {Y/N}  -->  ") == "Y" or input("\nDid the violation occur in a construction zone?  {Y/N}  -->  ") == "Y": ticketAmount *= 2
print("\nTicket amount:  $", ticketAmount, sep="")