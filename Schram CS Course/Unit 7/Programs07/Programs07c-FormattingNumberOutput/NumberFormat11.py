# NumberFormat11.py
# This program demonstrates that real numbers can be
# formatted with leading spaces, rounded digits past
# the decimal point, commas, and even dollar sign$.

hoursWorked = 50
hourlyRate = 199.98
grossPay = hoursWorked * hourlyRate
deductions = grossPay * 0.29
netPay = grossPay - deductions

print()
print("Hours Worked:",hoursWorked)
print("Hourly Rate: ","${:8,.2f}".format(hourlyRate))
print("Gross Pay:   ","${:8,.2f}".format(grossPay))
print("Deductions:  ","${:8,.2f}".format(deductions))
print("Net Pay:     ","${:8,.2f}".format(netPay))
