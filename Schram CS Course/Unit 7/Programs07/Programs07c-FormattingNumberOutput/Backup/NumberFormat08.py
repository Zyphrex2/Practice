# NumberFormat08.py
# This program repeats Documentation02.py from Chapter 3.
# One problem with the program still has is that the 
# numbers which are displayed represent money, but they 
# are not rounded to 2 decimal places.


hoursWorked = 35
hourlyRate = 8.75
grossPay = hoursWorked * hourlyRate
deductions = grossPay * 0.29
netPay = grossPay - deductions

print()
print("Hours Worked: ",hoursWorked)
print("Hourly Rate:  ",hourlyRate)
print("Gross Pay:    ",grossPay)
print("Deductions:   ",deductions)
print("Net Pay:      ",netPay)
