#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Problem 3 - number pyramids part one and part two

def print_number_pyramid():
    try:
        n = int(input("Enter max number: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        print("\nPart I")
        for i in range(1, n + 1): print(str(i) * i, i)     # increase then decrease
        for i in range(n - 1, 0, -1): print(str(i) * i, i)
        print("\nPart II")
        for i in range(n, 0, -1): print(str(i) * i, i)     # start from top down
        for i in range(2, n + 1): print(str(i) * i, i)     # then back up
    except ValueError:
        print("Invalid input. Enter a valid integer.")

if __name__ == "__main__":
    print_number_pyramid()