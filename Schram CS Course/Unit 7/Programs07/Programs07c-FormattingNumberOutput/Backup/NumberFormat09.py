# NumberFormat09.py
# This program demonstrates how to format real number
# output with the <format> command.  The f inside 
# "{:6.2f}" means this is a "floating-point number"
# which is the same thing as a "real number".  
# The 6 indicates the entire number will be 6 characters
# long, including the decimal point.  The 2 indicates
# there will be 2 digits after the decimal point.


hoursWorked = 35
hourlyRate = 8.75
grossPay = hoursWorked * hourlyRate
deductions = grossPay * 0.29
netPay = grossPay - deductions

print()
print("Hours Worked:","{:6.2f}".format(hoursWorked))
print("Hourly Rate: ","{:6.2f}".format(hourlyRate))
print("Gross Pay:   ","{:6.2f}".format(grossPay))
print("Deductions:  ","{:6.2f}".format(deductions))
print("Net Pay:     ","{:6.2f}".format(netPay))
