#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Get valid score between 0 and 100
def get_score(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a valid number.")

# Collect five scores
scores = []
for i in range(1, 6):
    score = get_score(f"Enter score {i}: ")
    scores.append(score)

# Calculate average
average = sum(scores) / len(scores)
print(f"\nAverage score: {average:.2f}")

# Assign letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Grade: {grade}")