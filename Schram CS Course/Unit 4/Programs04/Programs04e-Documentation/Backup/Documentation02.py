# Documentation02.py
# This program does exactly the same thing  
# as the previous program.  By using self-
# documenting variables, the program is 
# much easier to read and understand.


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
 