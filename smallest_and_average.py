"""
Program: Smallest Number & Average (User-Decided Count)
Author: Donaven Bruce
Description: Prompts for how many numbers to enter, reads that many integers,
tracks the running total and the smallest value, then prints the smallest
number and the average.
"""

# counter and total count
numbers_entered_count = 0
numbers_to_enter = int(input("How many numbers do you want to enter?:\n"))

# first number seeds smallest and total
number_input = int(input("Please enter your number: \n"))
smallest_number = number_input
total_sum = number_input

# collect remaining numbers 
while numbers_entered_count < numbers_to_enter - 1:
    number_input = int(input("Please enter your number: \n"))
    total_sum = total_sum + number_input
    if number_input < smallest_number:
        smallest_number = number_input
    numbers_entered_count = numbers_entered_count + 1

# average from total and count
average_value = total_sum / numbers_to_enter

print("*****")
print("The smallest number is:", smallest_number)
print("The average is:", average_value)
