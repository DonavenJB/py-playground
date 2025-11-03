"""
Program: Salary Accumulator for Five People
Author: Donaven Bruce
Description: Prompts for five yearly salaries, adds each to a running total,
and displays the total after each entry (accumulation concept).
"""

# start running total
total = 0

# get first salary, add to total, show total
yearly_salary = int(input("Please enter the first person's yearly salary: \n"))
total = total + yearly_salary
print("The total salary so far is: " + str(total))

# get second salary, add to total, show total
yearly_salary = int(input("Please enter the second person's yearly salary: \n"))
total = total + yearly_salary
print("The total salary so far is: " + str(total))

# get third salary, add to total, show total
yearly_salary = int(input("Please enter the third person's yearly salary: \n"))
total = total + yearly_salary
print("The total salary so far is: " + str(total))

# get fourth salary, add to total, show total
yearly_salary = int(input("Please enter the fourth person's yearly salary: \n"))
total = total + yearly_salary
print("The total salary so far is: " + str(total))

# get fifth salary, add to total, show total
yearly_salary = int(input("Please enter the fifth person's yearly salary: \n"))
total = total + yearly_salary
print("The total salary so far is: " + str(total))
