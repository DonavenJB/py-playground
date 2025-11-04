"""
Program: Net Salary Calculator with Tiered Taxes
Author: Donaven Bruce
Description: Asks for an employee name and salary, applies state tax and a
federal tax rate based on a 100000 threshold, then prints taxes and net salary.
"""

# tax rate constants
FED_TAX_RATE_HIGH = 0.20   # used when salary > 100000
FED_TAX_RATE_LOW = 0.15    # used when salary <= 100000
STATE_TAX_RATE = 0.05

# inputs
employee_name = input("Please enter your name : \n")
salary = int(input("Please enter your salary : \n"))

# compute state tax
state_tax = salary * STATE_TAX_RATE

# choose federal rate by salary tier and compute net
if salary > 100000:
    federal_tax = salary * FED_TAX_RATE_HIGH
    net_salary = salary - (federal_tax + state_tax)
    print("Your Federal Tax is :" + str(federal_tax))
    print("Your State Tax is :" + str(state_tax))
    print("Your net salary is :" + str(net_salary))
else:
    federal_tax = salary * FED_TAX_RATE_LOW
    net_salary = salary - (federal_tax + state_tax)
    print("Your Federal Tax is :" + str(federal_tax))
    print("Your State Tax is :" + str(state_tax))
    print("Your net salary is :" + str(net_salary))
