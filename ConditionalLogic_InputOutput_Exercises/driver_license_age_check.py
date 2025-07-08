#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Get valid age
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid. Enter a whole number.")

# Check eligibility
if 18 <= age <= 95:
    print("-" * 30)
    print(f"Your age is {age}.")
    print("You are eligible for a driver's license.")
    print("-" * 30)
else:
    print("-" * 30)
    print(f"Your age is {age}.")
    if age < 18:
        print("You must be at least 18.")
    else:
        print("Age exceeds the maximum of 95.")
    print("You are not eligible.")
    print("-" * 30)