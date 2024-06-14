# NumberFormat10.py
# This program demonstrates how to format 
# real numbers without leading spaces.


hoursWorked = 35
hourlyRate = 8.75
grossPay = hoursWorked * hourlyRate
deductions = grossPay * 0.29
netPay = grossPay - deductions

print()
print("Hours Worked:","{:.2f}".format(hoursWorked))
print("Hourly Rate: ","{:.2f}".format(hourlyRate))
print("Gross Pay:   ","{:.2f}".format(grossPay))
print("Deductions:  ","{:.2f}".format(deductions))
print("Net Pay:     ","{:.2f}".format(netPay))
