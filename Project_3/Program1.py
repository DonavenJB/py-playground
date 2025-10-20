# Program 1: NETSALARY
# Donaven Bruce
# My program asks for name, salary, and state for 6 employees.
# Calculates federal tax, state tax, and net salary with simple input validation.

ordinals = ["first", "second", "third", "fourth", "fifth", "sixth"]

for i in range(6):
    # get name (non-empty)
    print("Please enter the name of the " + ordinals[i] + " employee :")
    employee_name = input().strip()
    while employee_name == "":
        print("Name cannot be empty. Please enter the name of the " + ordinals[i] + " employee :")
        employee_name = input().strip()

    # get salary (number >= 0)
    print("Please enter the salary of the " + ordinals[i] + " employee :")
    salary_text = input().strip()
    while True:
        try:
            salary = float(salary_text)
            if salary < 0:
                print("Salary must be zero or positive. Please enter the salary of the " + ordinals[i] + " employee :")
                salary_text = input().strip()
            else:
                break
        except:
            print("Please enter a valid number. Enter the salary of the " + ordinals[i] + " employee :")
            salary_text = input().strip()

    # get state (2 letters). we normalize with upper() as instructed.
    print("Please enter the state (like CA, NV, AZ, or TX) of the " + ordinals[i] + " employee :")
    state = input().strip().upper()
    while not (len(state) == 2 and state.isalpha()):
        print("Please enter a valid 2-letter state code. Enter the state of the " + ordinals[i] + " employee :")
        state = input().strip().upper()

    # federal tax
    if salary > 100000:
        federal_tax = salary * 0.20
    else:
        federal_tax = salary * 0.15

    # state tax (10% for CA/NV/AZ/TX, otherwise 12%)
    if state == "CA" or state == "NV" or state == "AZ" or state == "TX":
        state_tax = salary * 0.10
    else:
        state_tax = salary * 0.12

    net_salary = salary - federal_tax - state_tax

    # results for this employee
    print("Employee: " + employee_name)
    print("Federal tax: " + str(round(federal_tax, 2)))
    print("State tax: " + str(round(state_tax, 2)))
    print("Net salary: " + str(round(net_salary, 2)))
    print("--------------------------------")
