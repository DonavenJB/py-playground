def function1():
    # Sums two integers and returns the result.
    try:
        num1 = int(input("Enter first integer: "))
        num2 = int(input("Enter second integer: "))
        return num1 + num2
    except ValueError:
        print("Error: Invalid input.")

def function2():
    # Subtracts the second integer from the first and returns the result.
    try:
        num1 = int(input("Enter first integer: "))
        num2 = int(input("Enter second integer: "))
        return num1 - num2
    except ValueError:
        print("Error: Invalid input.")

def function3():
    # Multiplies two integers and returns the result.
    try:
        num1 = int(input("Enter first integer: "))
        num2 = int(input("Enter second integer: "))
        return num1 * num2
    except ValueError:
        print("Error: Invalid input.")

def function4():
    # Divides the first integer by the second, handling division by zero.
    try:
        num1 = int(input("Enter first integer: "))
        num2 = int(input("Enter second integer: "))
        if num2 == 0:
            print("CRITICAL ERROR: Cannot divide by zero.")
            return None
        return num1 / num2
    except ValueError:
        print("Error: Invalid input.")

def function5():
    # Calculates the modulus, handling division by zero.
    try:
        num1 = int(input("Enter first integer: "))
        num2 = int(input("Enter second integer: "))
        if num2 == 0:
            print("CRITICAL ERROR: Cannot calculate modulus with zero divisor.")
            return None
        return num1 % num2
    except ValueError:
        print("Error: Invalid input.")

def function6():
    # Calculates integer division, handling division by zero.
    try:
        num1 = int(input("Enter first integer: "))
        num2 = int(input("Enter second integer: "))
        if num2 == 0:
            print("CRITICAL ERROR: Cannot perform integer division by zero.")
            return None
        return num1 // num2
    except ValueError:
        print("Error: Invalid input.")

def function7():
    # Calculates exponentiation.
    try:
        num1 = int(input("Enter base integer: "))
        num2 = int(input("Enter exponent integer: "))
        return num1 ** num2
    except ValueError:
        print("Error: Invalid input.")

def function8():
    # Calculates the average of a user-specified count of integers.
    running_total = 0
    entered_numbers = []
    
    while True:
        try:
            count = int(input("Enter number of values for average: "))
            if count < 0:
                print("Error: Count must be positive.")
                continue
            break
        except ValueError:
            print("Error: Invalid input for count.")

    if count == 0:
        print("No numbers to average.")
        return 0.0, 0.0, entered_numbers
    
    for i in range(count):
        while True:
            try:
                num = int(input(f"Enter integer {i + 1}: "))
                running_total += num
                entered_numbers.append(num)
                break
            except ValueError:
                print("Error: Invalid input.")

    print("Horizontal:", end=" ")
    for i, num in enumerate(entered_numbers):
        print(num, end="")
        if i < len(entered_numbers) - 1:
            print(", ", end="")
    print()

    print("Vertical:")
    for num in entered_numbers:
        print(num)

    average = running_total / count
    
    return running_total, average, entered_numbers

def function0():
    # Prints exit message and allows the main loop to terminate.
    print("Quitting.")

def main():
    # Runs the main menu loop until the user chooses Option 0.
    choice_of_user = -1

    while choice_of_user != 0:
        print("\n**** MENU ****")

        try:
            choice_of_user = int(input(
                "1- Add\n"
                "2- Subtract\n"
                "3- Multiply\n"
                "4- Divide\n"
                "5- Modulus\n"
                "6- Int. Div.\n"
                "7- Exp.\n"
                "8- Average\n"
                "0- Quit\n"))

            result = None
            
            if 1 <= choice_of_user <= 7:
                if choice_of_user == 1:
                    result = function1()
                elif choice_of_user == 2:
                    result = function2()
                elif choice_of_user == 3:
                    result = function3()
                elif choice_of_user == 4:
                    result = function4()
                elif choice_of_user == 5:
                    result = function5()
                elif choice_of_user == 6:
                    result = function6()
                elif choice_of_user == 7:
                    result = function7()
                
                if result is not None:
                    print(f"Result: {result}")
            
            elif choice_of_user == 8:
                total, average, num_list = function8()
                
                if num_list:
                    print(f"Total: {total}")
                    print(f"Average: {average}")

            elif choice_of_user == 0:
                function0()
            
            else:
                print("Invalid choice. Try again (0-8).")

        except ValueError:
            print("\nError: Invalid input. Enter a number (0-8).")
            choice_of_user = -1

if __name__ == "__main__":
    main()