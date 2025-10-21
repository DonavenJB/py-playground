#Donaven Bruce
#Program 2: Student Grades
#My program asks how many students, gets each student's name and three scores,
# computes the average, assigns the letter grade by the given ranges, and prints it.

print("=== CS119 Student Grades ===")

# Ask how many students using whole number >= 0
while True:
    raw = input("How many students? ").strip()
    if raw.isdigit():
        n = int(raw)
        break
    print("Please enter a whole number 0 or greater.")

print()

# Loop for each student
for i in range(1, n + 1):
    print("--- Student", i, "of", n, "---")

    # Get non-empty name
    while True:
        name = input("Student name: ").strip()
        if name != "":
            break
        print("Name cannot be empty.")

    # validation for a single score between 0..100
    while True:
        s1_raw = input("Enter Exam 1 score (0-100): ").strip()
        try:
            s1 = float(s1_raw)
            if 0 <= s1 <= 100:
                break
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a number like 88 or 92.5.")

    while True:
        s2_raw = input("Enter Exam 2 score (0-100): ").strip()
        try:
            s2 = float(s2_raw)
            if 0 <= s2 <= 100:
                break
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a number like 88 or 92.5.")

    while True:
        s3_raw = input("Enter Exam 3 score (0-100): ").strip()
        try:
            s3 = float(s3_raw)
            if 0 <= s3 <= 100:
                break
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a number like 88 or 92.5.")

    # Compute average
    avg = (s1 + s2 + s3) / 3.0

    # Determine letter grade using exact ranges
    if 98 <= avg <= 100:
        grade = "A+"
    elif 95 <= avg < 98:
        grade = "A"
    elif 91 <= avg < 95:
        grade = "A-"
    elif 88 <= avg < 91:
        grade = "B+"
    elif 84 <= avg < 88:
        grade = "B"
    elif 80 <= avg < 84:
        grade = "B-"
    elif 75 <= avg < 80:
        grade = "C+"
    elif 70 <= avg < 75:
        grade = "C"
    elif 60 < avg < 70:
        grade = "D"
    else:
        grade = "NC"

    # Display result with average shown to two decimals
    print("Name:", name)
    print("Average:", format(avg, ".2f"))
    print("Grade:", grade)
    print()

print("=== Done ===")
