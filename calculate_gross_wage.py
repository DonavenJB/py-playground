"""
Program: Simple Gross Wage Calculator
Author: Donaven Bruce
Description: Prompts for a user's first/last name, hourly wage, and hours worked,
then calculates and prints the gross wage (hourly_wage * total_hours).
"""

# Ask for user inputs
last_name = input("What is your last name:\n")
first_name = input("What is your first name:\n")
hourly_wage = int(input("What is your hourly wage:\n"))
total_hours = int(input("How many hours have you worked:\n"))

# Compute gross wage
gross_wage = hourly_wage * total_hours

# Display results
print("Your first name is " + first_name + "\nYour last name is " + last_name +
      "\nYour wage is $" + str(gross_wage))
