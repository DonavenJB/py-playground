# Donaven Bruce

# CS 119

# Project 4 Program One



# Menu to manage a list of student names.

# Add, remove, insert, find max/min, and sort the list.



choice_of_user = 0 # 0 starts loop

studentFullName=["Mike navarro","Miguel saba","Maria Rami"] # List of names



# Main menu loop

while choice_of_user != 7:

    print("\n**** MENU OPTIONS ****")

    # Try block 

    try:

      # Get user choice as an integer

      choice_of_user = int(input(

          "1- Add an item to the list\n"

          "2- Remove an item from the list ==> ask for the name instead of index\n"

          "3- Insert an item into the list\n"

          "4- Find maximum\n"

          "5- Find the Minimum\n"

          "6- Sort the list in descending order\n"

          "7- Quit the program\n"))

      

      # Using if elif instead of user defined functions

      if choice_of_user == 1:

        # Add item

        print("\n-Current list-")

        for name in studentFullName:

            print(name)

        

        # Add new name to the end

        studentFullName.append(input("\nPlease enter the students full name:\n"))

        

        print("\n-Updated list-")

        for name in studentFullName:

            print(name)

        choice_of_user = 0 # Reset loop

        

      elif choice_of_user == 2:

        # Remove item

        print("\n-Current list-")

        for name in studentFullName:

            print(name)

            

        name_to_remove = input("\nEnter the name to remove from list\n")

        # Handle name not in list

        try:

            # Remove the item by value

            studentFullName.remove(name_to_remove)

            print("\n-Updated list-")

            for name in studentFullName:

                print(name)

        # Catch error if name not found

        except ValueError:

            print(f"\nError: '{name_to_remove}' was not found in the list.")

        choice_of_user = 0 # Reset loop

        

      elif choice_of_user == 3:

        # Insert item

        print("\n-Current list-")

        for name in studentFullName:

            print(name)

        

        # Handle non-numeric index

        try:

            # Get index as integer

            indexNum = int(input("\nWhere do you want to insert the item? (Enter the index number): "))

            name = input("\nPlease enter the value for the item you want to insert: ")

            

            # Insert name at index

            studentFullName.insert(indexNum, name)

            

            print("\n-Updated list-")

            for name in studentFullName:

                print(name)

        # Catch error if int() fails

        except ValueError:

            print("\nError: Invalid index. Please enter a whole number.")

        choice_of_user = 0 # Reset loop

        

      elif choice_of_user == 4:

        # Find Max

        print("\n-Current list-")

        for name in studentFullName:

            print(name)

            

        # Check if list is empty

        if studentFullName:

            # Find last name alphabetically

            find_max_result = max(studentFullName)

            print("\n" + find_max_result)

        else:

            print("\nThe list is empty. Cannot find a maximum value.")

        choice_of_user = 0 # Reset loop

        

      elif choice_of_user == 5:

        # Find Min

        print("\n-Current list-")

        for name in studentFullName:

            print(name)

            

        # Check if list is empty

        if studentFullName:

            # Find first name alphabetically

            find_min_result = min(studentFullName)

            print("\n" + find_min_result)

        else:

            print("\nThe list is empty. Cannot find a minimum value.")

        choice_of_user = 0 # Reset loop

        

      elif choice_of_user == 6:

        # Sort List

        print("\n-Current list-")

        for name in studentFullName:

            print(name)

            

        # Sort the list Z to A

        studentFullName.sort(reverse=True)

        

        print("\n-Updated list-")

        for name in studentFullName:

            print(name)

        choice_of_user = 0 # Reset loop

        

      elif choice_of_user == 7:

        # Quit

        print("Thank you for using the program.")

        print("Bye")

        # Loop will stop

        

      else:

        # Handle invalid numbers

        print("Invalid choice. Please try again!")

        choice_of_user = 0 # Reset loop

        

    # Runs if int() fails

    except ValueError:

      print("\nError: Invalid input. Please enter a number (1-7).")

      choice_of_user = 0 # Reset loop