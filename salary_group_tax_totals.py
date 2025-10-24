"""
Program: Salary Tax Summary (While Loop, Tiered Groups)
Author: Donaven Bruce
Description: Repeatedly prompts for one person's salary until the user stops.
Computes federal (0.20 if salary > 100000 else 0.15) and state (0.05) taxes,
prints taxes and net salary each time, counts people in four salary groups,
and finally prints group counts plus total state and federal tax.
"""

# group counters
over_100k_count = 0
ge_50k_lt_100k_count = 0
ge_25k_lt_50k_count = 0
lt_25k_count = 0

# tax rates
FED_TAX_RATE_HIGH = 0.20        # salary > 100000
FED_TAX_RATE_STANDARD = 0.15    # otherwise
STATE_TAX_RATE = 0.05

# accumulators
total_state_tax = 0
total_federal_tax = 0

# loop control
user_choice = "Yes"

# main loop
while user_choice == "yes" or user_choice == "Yes" or user_choice == "YES":
    salary = int(input("Please enter one persons salary: \n"))

    if salary > 100000:
        fed_tax = salary * FED_TAX_RATE_HIGH
        print("Your federal tax is :" + str(fed_tax))
        state_tax = salary * STATE_TAX_RATE
        print("Your state tax is :" + str(state_tax))
        net_salary = salary - (fed_tax + state_tax)
        over_100k_count = over_100k_count + 1
        total_state_tax = total_state_tax + state_tax
        total_federal_tax = total_federal_tax + fed_tax
        print("Your net salary is: " + str(net_salary))

    elif salary >= 50000 and salary < 100000:
        fed_tax = salary * FED_TAX_RATE_STANDARD
        print("Your federal tax is :" + str(fed_tax))
        state_tax = salary * STATE_TAX_RATE
        print("Your state tax is :" + str(state_tax))
        net_salary = salary - (fed_tax + state_tax)
        ge_50k_lt_100k_count = ge_50k_lt_100k_count + 1
        total_state_tax = total_state_tax + state_tax
        total_federal_tax = total_federal_tax + fed_tax
        print("Your net salary is: " + str(net_salary))

    elif salary >= 25000 and salary < 50000:
        fed_tax = salary * FED_TAX_RATE_STANDARD
        print("Your federal tax is :" + str(fed_tax))
        state_tax = salary * STATE_TAX_RATE
        print("Your state tax is :" + str(state_tax))
        net_salary = salary - (fed_tax + state_tax)
        ge_25k_lt_50k_count = ge_25k_lt_50k_count + 1
        total_state_tax = total_state_tax + state_tax
        total_federal_tax = total_federal_tax + fed_tax
        print("Your net salary is: " + str(net_salary))

    elif salary < 25000:
        fed_tax = salary * FED_TAX_RATE_STANDARD
        print("Your federal tax is :" + str(fed_tax))
        state_tax = salary * STATE_TAX_RATE
        print("Your state tax is :" + str(state_tax))
        net_salary = salary - (fed_tax + state_tax)
        lt_25k_count = lt_25k_count + 1
        total_state_tax = total_state_tax + state_tax
        total_federal_tax = total_federal_tax + fed_tax
        print("Your net salary is: " + str(net_salary))

    # continue?
    user_choice = input("Would you like to continue?(yes/no): \n")

# summaries
print("*****")
print("The number of people who earned more than 100000 is:  " + str(over_100k_count))
print("The number of people who earned More than or equal to 50000 and less than 100000 is:  " + str(ge_50k_lt_100k_count))
print("The number of people who earned More than or equal to 25000 and less than 50000 is:  " + str(ge_25k_lt_50k_count))
print("The number of people who earned Below 25000 is:  " + str(lt_25k_count))
print("The total state tax is: " + str(total_state_tax))
print("The total federal tax is: " + str(total_federal_tax))
