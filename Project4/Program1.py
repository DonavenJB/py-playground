# Donaven Bruce
# CS 119
# Project 4 Program One

# This program is a menu that lets a user manage a list of student names.
# It can add, remove, insert, find max/min, and sort the list.

choice_of_user = 0 # Holds menu choice, 0 starts the loop
studentFullName=["Mike navarro","Miguel saba","Maria Rami"] # Global list of names

def print_current_list():
  print("\n-Current list-")
  # Loop and print every name
  for name in studentFullName:
      print(name)

def print_updated_list():
  print("\n-Updated list-")
  # Helper function to print the list after a change
  for name in studentFullName:
      print(name)
  
def add_to_list():
    print_current_list()
    # Add new name to the end of the list
    studentFullName.append(input("\nPlease enter the students full name:\n"))
    print_updated_list()

def delete_from_list():
  print_current_list()
  name_to_remove = input("\nEnter the name to remove from list\n")
  # Try block handles a name not being found
  try:
    # Remove the item by its value
    studentFullName.remove(name_to_remove)
    print_updated_list()
  # Catch the error if the name was not in the list
  except ValueError:
    print(f"\nError: '{name_to_remove}' was not found in the list.")

def insert_to_list():
  print_current_list()
  # Try block handles a non-numeric index
  try:
    # Convert index from string to integer
    indexNum = int(input("\nWhere do you want to insert the item? (Enter the index number): "))
    name = input("\nPlease enter the value for the item you want to insert: ")
    # Insert the name at the specified index
    studentFullName.insert(indexNum, name)
    print_updated_list()
  # Catch the error if int() fails
  except ValueError:
    print("\nError: Invalid index. Please enter a whole number.")

def find_max():
  print_current_list()
  # Check if the list is empty first
  if studentFullName:
    # Find the last name alphabetically
    find_max_result = max(studentFullName)
    print("\n" + find_max_result)
  # Handle the empty list case
  else:
    print("\nThe list is empty. Cannot find a maximum value.")

def find_min():
  print_current_list()
  # Check if the list is empty first
  if studentFullName:
    # Find the first name alphabetically
    find_min_result = min(studentFullName)
    print("\n" + find_min_result)
  else:
    print("\nThe list is empty. Cannot find a minimum value.")

def sort_list():
  print_current_list()
  # Sort the list in-place
  # reverse=True makes it descending Z to A
  studentFullName.sort(reverse=True)
  print_updated_list()
  
def list_of_options(choice_of_user):
  # Main menu loop
  # Keeps running until user chooses 7
  while choice_of_user != 7:
    print("\n**** MENU OPTIONS ****")
    # A try block catches non-number inputs
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
      
      # if/elif block calls the correct function
      if choice_of_user == 1:
        add_to_list()
        choice_of_user = 0 # Reset choice to continue loop
      elif choice_of_user == 2:
        delete_from_list()
        choice_of_user = 0 # Reset choice
      elif choice_of_user == 3:
        insert_to_list()
        choice_of_user = 0 # Reset choice
      elif choice_of_user == 4:
        find_max()
        choice_of_user = 0 # Reset choice
      elif choice_of_user == 5:
        find_min()
        choice_of_user = 0 # Reset choice
      elif choice_of_user == 6:
        sort_list()
        choice_of_user = 0 # Reset choice
      elif choice_of_user == 7:
        # This choice exits the loop
        print("Thank you for using the program.")
        print("Bye")
      else:
        # Handle numbers other than 1-7
        print("Invalid choice. Please try again!")
        choice_of_user = 0 # Reset choice
        
    # Runs if int() conversion fails
    except ValueError:
      print("\nError: Invalid input. Please enter a number (1-7).")
      choice_of_user = 0 # Reset choice
  return choice_of_user


# This line starts the program
# It calls the main menu function
choice_of_user = list_of_options(choice_of_user)