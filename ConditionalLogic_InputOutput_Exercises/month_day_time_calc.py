# Get valid integer in range
def get_int_input(prompt, min_val, max_val):
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            print(f"Input must be between {min_val} and {max_val}. Try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Ask for month number
month_num = get_int_input("Enter the month number 1=Jan, 12=Dec: ", 1, 12)

days = 0
month_name = ""

# Set month name and days
if month_num == 1:
    month_name = "January"
    days = 31
elif month_num == 2:
    month_name = "February"
    is_leap = get_int_input("Is this a leap year? Enter 1 for Yes, 0 for No: ", 0, 1)
    days = 29 if is_leap else 28
elif month_num == 3:
    month_name = "March"
    days = 31
elif month_num == 4:
    month_name = "April"
    days = 30
elif month_num == 5:
    month_name = "May"
    days = 31
elif month_num == 6:
    month_name = "June"
    days = 30
elif month_num == 7:
    month_name = "July"
    days = 31
elif month_num == 8:
    month_name = "August"
    days = 31
elif month_num == 9:
    month_name = "September"
    days = 30
elif month_num == 10:
    month_name = "October"
    days = 31
elif month_num == 11:
    month_name = "November"
    days = 30
else:
    month_name = "December"
    days = 31

# Convert days to hours, minutes, seconds
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Show result
print(f"{month_name} is the {month_num}th month.")
print(f"This month has {days} days, {hours} hrs, {minutes} min, {seconds} sec.")