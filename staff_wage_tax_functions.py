"""
Program: Staff Wages, Federal/State Tax, and Net Pay (Functions)
Author: Donaven Bruce
Description: Prompts for hours, hourly rate, state, and marital status. Computes
wages, federal tax (by status), state tax (by state group), and prints wages,
taxes, and net pay.
"""

def calculate_wages(staff_hours, staff_hourly_rate):
    # wages = hours * rate
    staff_wages_earned = staff_hours * staff_hourly_rate
    return staff_wages_earned

def calculate_federal_tax(wages_earned, relationship_status):
    # tax by marital status
    if relationship_status == "Married":
        staff_fed_tax_bill = wages_earned * .20
    elif relationship_status == "Single":
        staff_fed_tax_bill = wages_earned * .25
    elif relationship_status != "Married" or relationship_status != "Single":
        staff_fed_tax_bill = wages_earned * .22
    return staff_fed_tax_bill

def calculate_state_tax(staff_wages, staff_state):
    # state groupings with fixed rates
    if staff_state == "CA" or staff_state == "NV" or staff_state == "SD" or staff_state == "WA" or staff_state == "AZ":
        staff_state_tax_bill = staff_wages * 0.08
    elif staff_state == "TX" or staff_state == "IL" or staff_state == "MO" or staff_state == "OH" or staff_state == "VA":
        staff_state_tax_bill = staff_wages * 0.07
    elif staff_state == "NM" or staff_state == "OR" or staff_state == "IN":
        staff_state_tax_bill = staff_wages * 0.06
    elif staff_state != "NM" or staff_state != "OR" or staff_state != "IN" or staff_state != "TX" or staff_state != "IL" or staff_state != "MO" or staff_state != "OH" or staff_state != "VA" or staff_state != "CA" or staff_state != "NV" or staff_state != "SD" or staff_state != "WA" or staff_state != "AZ":
        staff_state_tax_bill = staff_wages * 0.05
    return staff_state_tax_bill

def calculate_net(staff_wages, staff_fed_tax, staff_state_tax):
    # net = wages - (federal + state)
    staff_wages_net = staff_wages - (staff_fed_tax + staff_state_tax)
    print("**********")
    print("Your wage is: $" + str(staff_wages),
          "\nYour federal tax is: $" + str(staff_fed_tax),
          "\nYour state tax is: $" + str(staff_state_tax),
          "\nYour net wage is: $" + str(staff_wages_net))
    print("**********")

# inputs
staff_hours_worked = int(input("Please enter your work hours: \n"))
staff_hourly_rate = int(input("Please enter your hourly rate: \n"))
staff_state_of_residence = input("Please enter your state of residence: \n")
staff_relationship_status = input("Please enter your marital status: \n")

# calculations
staff_wages = calculate_wages(staff_hours_worked, staff_hourly_rate)
staff_federal_tax = calculate_federal_tax(staff_wages, staff_relationship_status)
staff_state_tax = calculate_state_tax(staff_wages, staff_state_of_residence)

# output
calculate_net(staff_wages, staff_federal_tax, staff_state_tax)
