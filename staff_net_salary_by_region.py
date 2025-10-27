"""
Program: Staff Net Salary by Region (5 Employees)
Author: Donaven Bruce
Description: Prompts for name, salary, and state for five employees. Applies a
federal rate (0.20 if salary > 100000, else 0.15) and a state rate based on
listed states per region; otherwise 0.12. Prints federal tax, state tax, and net salary.
"""

# federal tax rates
FED_TAX_RATE_RICH = 0.20          # salary > 100000
FED_TAX_RATE_POOR = 0.15          # salary <= 100000

# state/region tax rates
WESTERN_REGION_STATE_TAX_RATE = 0.10
SOUTHERN_REGION_STATE_TAX_RATE = 0.09
EASTERN_REGION_STATE_TAX_RATE  = 0.08
OTHER_WISE_STATE_TAX           = 0.12  # all other states

for x in range(1, 6):
    # inputs
    member_of_staff_name = input("Please enter employee Name: \n")
    member_of_staff_salary = int(input("Please enter employee salary: \n"))
    member_of_staff_state = input("Please enter employee state: \n")

    # federal tax
    if member_of_staff_salary > 100000:
        member_of_staff_fed_tax_calculated = member_of_staff_salary * FED_TAX_RATE_RICH
        print(member_of_staff_name + " federal tax is: " + str(member_of_staff_fed_tax_calculated))
    else:
        member_of_staff_fed_tax_calculated = member_of_staff_salary * FED_TAX_RATE_POOR
        print(member_of_staff_name + " federal tax is: " + str(member_of_staff_fed_tax_calculated))

    # state tax by region
    if member_of_staff_state == "Newyork" or member_of_staff_state == "Illinois" or member_of_staff_state == "Wisconsin" or member_of_staff_state == "Delaware":
        member_of_staff_state_tax_calculated = member_of_staff_salary * EASTERN_REGION_STATE_TAX_RATE
        print(member_of_staff_name + " state tax is: " + str(member_of_staff_state_tax_calculated))
    elif member_of_staff_state == "California" or member_of_staff_state == "Arizona" or member_of_staff_state == "Washington" or member_of_staff_state == "Nevada":
        member_of_staff_state_tax_calculated = member_of_staff_salary * WESTERN_REGION_STATE_TAX_RATE
        print(member_of_staff_name + " state tax is: " + str(member_of_staff_state_tax_calculated))
    elif member_of_staff_state == "Texas" or member_of_staff_state == "Alabama" or member_of_staff_state == "Newmexico":
        member_of_staff_state_tax_calculated = member_of_staff_salary * SOUTHERN_REGION_STATE_TAX_RATE
        print(member_of_staff_name + " state tax is: " + str(member_of_staff_state_tax_calculated))
    else:
        member_of_staff_state_tax_calculated = member_of_staff_salary * OTHER_WISE_STATE_TAX
        print(member_of_staff_name + " state tax is: " + str(member_of_staff_state_tax_calculated))

    # net salary
    member_of_staff_net_salary = member_of_staff_salary - member_of_staff_fed_tax_calculated - member_of_staff_state_tax_calculated
    print(member_of_staff_name + " net salary is: " + str(member_of_staff_net_salary))
    print("*****")
