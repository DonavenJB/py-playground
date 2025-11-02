"""
Program: Simple Total Cost Calculator
Author: Donaven Bruce
Description: Asks the user for the prices of three items,
adds them, and displays the total.
"""

# Get prices for three items
item1 = int(input("Enter price of the first Item:$\n"))
item2 = int(input("Enter price of the second item:$\n"))
item3 = int(input("Enter price of the third item:$\n"))

# Add the three prices
total = item1 + item2 + item3

# Show the total to the user
print("Total price for all three items:$ " + str(total))
