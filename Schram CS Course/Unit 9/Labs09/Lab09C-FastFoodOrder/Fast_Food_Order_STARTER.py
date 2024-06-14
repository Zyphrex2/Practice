# Program:  Fast_Food_Order
# Purpose:  Compute the total of a fast food order from the 
# burgers, drinks, and chips that a customer orders

# These variables are considered constants, use these variables
# wherever the cost is used, do not type in these values anywhere else.
COST_OF_BURGER = 3.25
COST_OF_DRINK = 1.75
COST_OF_CHIPS = 1.00

# computeTotal is a FUNCTION, it will take 3 values needed as 
# PARAMETERS, use them to compute the order total cost, and 
# return the total
def computeTax(total):
   return total * 0.0825

def computeTotal(burgers, drinks, chips):
   totalCost = 0.0
   totalCost+=burgers*COST_OF_BURGER
   totalCost+=drinks*COST_OF_DRINK
   totalCost+=chips*COST_OF_CHIPS
   totalCost+=computeTax(totalCost)
            
   return totalCost

############### MAIN PROGRAM #########################

numberOfBurgers = 3
numberOfDrinks = 5
numberOfChips = 4

# Update the FUNCTION CALL with the ARGUMENTS needed.
# Use the variables provided.

total = computeTotal(numberOfBurgers, numberOfDrinks, numberOfChips)
format(total, '0.2f')
print("Order Total: $", format(total, '0.2f'))
print()

# Add two more calls to computeTotal with different ARGUMENTS
# along with print statements.

numberOfBurgers = 5
numberOfDrinks = 4
numberOfChips = 3

total = computeTotal(numberOfBurgers, numberOfDrinks, numberOfChips)
print("Order Total: $", format(total, '0.2f'))
print()


numberOfBurgers = 4
numberOfDrinks = 3
numberOfChips = 5

total = computeTotal(numberOfBurgers, numberOfDrinks, numberOfChips)
print("Order Total: $", format(total, '0.2f'))
print()