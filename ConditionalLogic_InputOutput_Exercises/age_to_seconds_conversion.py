#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

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

# Get age components
years = get_int_input("Enter years: ", 0, 150)
days = get_int_input("Enter additional days: ", 0, 365)
hours = get_int_input("Enter additional hours: ", 0, 23)

# Constants
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR
SECONDS_PER_DAY = SECONDS_PER_HOUR * HOURS_PER_DAY

# Without considering leap years 
seconds_no_leap = (
    years * 365 * SECONDS_PER_DAY +
    days * SECONDS_PER_DAY +
    hours * SECONDS_PER_HOUR
)

# With leap years 
seconds_with_leap = (
    years * 365.25 * SECONDS_PER_DAY +
    days * SECONDS_PER_DAY +
    hours * SECONDS_PER_HOUR
)

# Display both results clearly
print("\n" + "="*50)
print(f"Age: {years} years, {days} days, {hours} hours")
print("="*50)
print(f"Total seconds (ignoring leap years)   : {int(seconds_no_leap):,}")
print(f"Total seconds (including leap years) : {int(seconds_with_leap):,}")
print("="*50)