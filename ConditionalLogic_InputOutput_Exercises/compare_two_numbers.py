#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Get valid float number
def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value != value or value == float('inf') or value == float('-inf'):
                raise ValueError
            return value
        except ValueError:
            print("Invalid. Enter a valid number.")

# Read two numbers
number1 = get_number("Enter the first number: ")
number2 = get_number("Enter the second number: ")

# Compare and print result
if number1 > number2:
    print(f"{number1} is greater than {number2}.")
elif number1 < number2:
    print(f"{number1} is less than {number2}.")
else:
    print(f"{number1} is equal to {number2}.")