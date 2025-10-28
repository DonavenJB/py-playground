"""
Program: Metro Bus Riders, Fare, and Profit (Functions)
Author: Donaven Bruce
Description: Prompts for passengers on three buses, totals all riders, computes
total fare at $2.50 per rider, then computes net profit assuming operating
costs are 50% of fare. Displays totals.
"""

def accumulate_all_commuters(num_commuters_one, num_commuters_two, num_commuters_three):
    # total riders across three buses
    commuters_accumulated = (num_commuters_one + num_commuters_two + num_commuters_three)
    return commuters_accumulated

def accumulate_all_commuter_fare(num_of_all_commuters):
    # fare = riders * 2.50
    commuter_accumulated_fare = num_of_all_commuters * 2.50
    return commuter_accumulated_fare

def profit_from_fare_calculator(total_commuter_fare):
    # profit = fare - 50% operating cost
    metro_bus_profit_ = total_commuter_fare - (total_commuter_fare * 0.5)
    return metro_bus_profit_

# inputs
num_of_bus_commuters_one = int(input("Please enter the number of passengers for bus1 :\n"))
num_of_bus_commuters_two = int(input("Please enter the number of passengers for bus2 :\n"))
num_of_bus_commuters_three = int(input("Please enter the number of passengers for bus3 :\n"))

# calculations
total_commuters = accumulate_all_commuters(num_of_bus_commuters_one, num_of_bus_commuters_two, num_of_bus_commuters_three)
total_fare = accumulate_all_commuter_fare(total_commuters)
net_profit = profit_from_fare_calculator(total_fare)

# outputs
print("***********")
print("There are total " + str(total_commuters) + " passengers from three buses.")
print("The total fare earned is: $" + str(total_fare))
print("The net profit is: $" + str(net_profit))
print("***********")
