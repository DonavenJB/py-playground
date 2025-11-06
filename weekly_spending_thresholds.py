"""
Program: Weekly Spending Threshold Counter
Author: Donaven Bruce
Description: Prompts for daily food and gas spending (Mon–Sun),
counts how many days food > $20 and gas > $10, then displays the counts.
"""

# counters for days exceeding thresholds
food_expensive_days_count = 0
gas_expensive_days_count = 0

# inputs for each day (food then gas)
monday_food_spend = int(input("Please enter the amount spent on food on Monday :\n"))
monday_gas_spend = int(input("Please enter the amount spent on gas on Monday :\n"))

tuesday_food_spend = int(input("Please enter the amount spent on food on Tuesday :\n"))
tuesday_gas_spend = int(input("Please enter the amount spent on gas on Tuesday :\n"))

wednesday_food_spend = int(input("Please enter the amount spent on food on Wednesday :\n"))
wednesday_gas_spend = int(input("Please enter the amount spent on gas on Wednesday :\n"))

thursday_food_spend = int(input("Please enter the amount spent on food on Thursday :\n"))
thursday_gas_spend = int(input("Please enter the amount spent on gas on Thursday :\n"))

friday_food_spend = int(input("Please enter the amount spent on food on Friday :\n"))
friday_gas_spend = int(input("Please enter the amount spent on gas on Friday :\n"))

saturday_food_spend = int(input("Please enter the amount spent on food on Saturday :\n"))
saturday_gas_spend = int(input("Please enter the amount spent on gas on Saturday :\n"))

sunday_food_spend = int(input("Please enter the amount spent on food on Sunday :\n"))
sunday_gas_spend = int(input("Please enter the amount spent on gas on Sunday :\n"))

# threshold checks (food > 20, gas > 10); increment counters
if monday_food_spend > 20:
    food_expensive_days_count = food_expensive_days_count + 1
if monday_gas_spend > 10:
    gas_expensive_days_count = gas_expensive_days_count + 1

if tuesday_food_spend > 20:
    food_expensive_days_count = food_expensive_days_count + 1
if tuesday_gas_spend > 10:
    gas_expensive_days_count = gas_expensive_days_count + 1

if wednesday_food_spend > 20:
    food_expensive_days_count = food_expensive_days_count + 1
if wednesday_gas_spend > 10:
    gas_expensive_days_count = gas_expensive_days_count + 1

if thursday_food_spend > 20:
    food_expensive_days_count = food_expensive_days_count + 1
if thursday_gas_spend > 10:
    gas_expensive_days_count = gas_expensive_days_count + 1

if friday_food_spend > 20:
    food_expensive_days_count = food_expensive_days_count + 1
if friday_gas_spend > 10:
    gas_expensive_days_count = gas_expensive_days_count + 1

if saturday_food_spend > 20:
    food_expensive_days_count = food_expensive_days_count + 1
if saturday_gas_spend > 10:
    gas_expensive_days_count = gas_expensive_days_count + 1

if sunday_food_spend > 20:
    food_expensive_days_count = food_expensive_days_count + 1
if sunday_gas_spend > 10:
    gas_expensive_days_count = gas_expensive_days_count + 1

# final summaries
print("You spent more than 20 dollars per day on food in " +
      str(food_expensive_days_count) + " days of the week.")
print("You spent more than 10 dollars per day on gas in " +
      str(gas_expensive_days_count) + " days of the week.")
