#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Problem 2 - star diamond pattern with matching numbers

def print_star_diamond():
    try:
        n = int(input("Enter pattern size: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        for i in range(1, n + 1):
            print("*" * i, i)               # build upper half, i stars per row
        for i in range(n - 1, 0, -1):
            print("*" * i, i)               # build lower half, decreasing
    except ValueError:
        print("Invalid input. Enter a valid integer.")

if __name__ == "__main__":
    print_star_diamond()