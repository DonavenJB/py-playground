#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Problem 1 - print n by n stars with row numbers and total

def print_star_rows():
    try:
        n = int(input("Please enter an integer value: "))
        for i in range(1, n + 1):
            print("*" * n, i)               # n stars followed by current row number
        print(f"\nYou displayed {n * n} stars.")  # total stars is n squared
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    print_star_rows()