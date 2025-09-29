# Donaven Bruce
# Program 2: My program accepts the yearly salary of five employees (one at a time)
#            Here we are using the accumulation concept to calculate and display the total 
#            salary from all employees combined

total_salaries_combined = 0

#gather data for first person
salary = float(input("Please enter the first person's yearly salary: \n"))
total_salaries_combined = total_salaries_combined + salary #accumulation

print("accumulated salary: so far is: " + str(total_salaries_combined)) # print to user

#gather data for second person
salary = float(input("Please enter the second person's yearly salary: \n"))
total_salaries_combined = total_salaries_combined + salary #accumulation

print("accumulated salary: so far is: " + str(total_salaries_combined)) #print to user

#gather data for third person
salary = float(input("Please enter the third person's yearly salary: \n")) 
total_salaries_combined = total_salaries_combined + salary #accumulation

print("accumulated salary: so far is: " + str(total_salaries_combined)) #print to user

#gather data for fourth person
salary = float(input("Please enter the fourth person's yearly salary: \n"))
total_salaries_combined = total_salaries_combined + salary #accumulation

print("accumulated salary: so far is: " + str(total_salaries_combined)) #print to user

#gather data for fift person
salary = float(input("Please enter the fifth person's yearly salary: \n"))
total_salaries_combined = total_salaries_combined + salary #accumulation

print("accumulated salary is: " + str(total_salaries_combined)) #final total including all five salaries
