# Program:  Logical Opertors:  NCAA Basketball Specification
# Purpose: Use conditional statements to determine if
# a given basketball meets NCAA specifications.
# Name:
# Period:

# Constants:  Specification Limits
LOW_SIZE_LIMIT = 29.5
HIGH_SIZE_LIMIT = 30.0
LOW_WEIGHT_LIMIT = 20.0
HIGH_WEIGHT_LIMIT = 22.0
LOW_PRESSURE_LIMIT = 7.5
HIGH_PRESSURE_LIMIT = 8.5

# Declare variables that will be needed
meetsWeightSpecs = False
meetsSizeSpecs = False
meetsPressureSpecs = False
meetsAllSpecs = False

# Get user input on size and weight of basketball
while True:
    size = float(input("Enter basketball size-inches circumference: "))
    weight = float(input("Enter basketball weight-oz: "))
    pressure = float(input("Enter basketball pressure-PSI: "))
    if not(0<size<50 or 0<weight<50 or 0<pressure<20):
        print("Invalid Input! Please try again.")
    else: break


# Check size and weight to set Boolean variables
meetsSizeSpecs = size >= LOW_SIZE_LIMIT and size <= HIGH_SIZE_LIMIT
meetsPressureSpecs = pressure >= LOW_PRESSURE_LIMIT and pressure <= HIGH_PRESSURE_LIMIT
meetsWeightSpecs = weight >= LOW_WEIGHT_LIMIT and weight <= HIGH_WEIGHT_LIMIT
meetsAllSpecs = meetsPressureSpecs and meetsSizeSpecs and meetsWeightSpecs
# Print summary report
print("\n\nBasketball Specification Report:\n")
print("Size (inches-circumference): ", size)
print("Weight (oz): ", weight)
print("Pressure (PSI): ", pressure)
print("Meets NCAA Regulations: ", meetsAllSpecs)
if not meetsAllSpecs:
    print("\nBasketball Failure Report:")
    print("Meets Size Range: ", meetsSizeSpecs)
    print("Meets Weight Range: ", meetsWeightSpecs) 
    print("Meets Pressure Range: ", meetsPressureSpecs)


print("Report Complete")