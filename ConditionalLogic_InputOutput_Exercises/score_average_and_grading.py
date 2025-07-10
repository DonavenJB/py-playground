#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Helper function to get a valid score
def get_score(prompt):
    while True:
        try:
            value = float(input(prompt))
            # Check for valid score range
            if 0 <= value <= 100:
                return value
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a valid number.")

# Gather 5 scores
scores = []
for i in range(1, 6):
    score = get_score(f"Enter score {i}: ")
    scores.append(score)

# Calculate average
average = sum(scores) / len(scores)

# Display average
print(f"\nAverage score: {average:.2f}")

# Assign grade using cascading logic
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