# Documentation03.py
# This program adds a multi-line comment at  
# the beginning to help explain the program.   
# Several short single-line comments are also 
# added to provide more detail for each variable.


"""
Payroll Program                                    
Written by Leon Schram 09-09-09                    
                                                    
This program takes the hours worked and hourly rate 
of an employee and computes the gross pay earned.   
Federal deductions are computed as 29% of gross pay.
Finally the take-home pay or net pay is computed by 
subtraction deductions from gross pay.               
"""


hoursWorked = 35   # hours worked per week
hourlyRate = 8.75  # pay rate earned per hour
grossPay = hoursWorked * hourlyRate  # total earnings
deductions = grossPay * 0.29         # federal tax
netPay = grossPay - deductions       # take home pay

print()
print("Hours Worked: ",hoursWorked)
print("Hourly Rate:  ",hourlyRate)
print("Gross Pay:    ",grossPay)
print("Deductions:   ",deductions)
print("Net Pay:      ",netPay)
