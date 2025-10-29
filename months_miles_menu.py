"""
Program: Month & Miles Menu (Populate, Search, Min/Max)
Author: Donaven Bruce
Description: Menu lets the user populate two arrays (12 month names and their
miles), search by month name, and display the smallest and largest miles.
"""

choice_of_user = ''
collection_of_months = []
collection_of_miles = []

def populate_the_arrays(months_collection, miles_collection):
  # read 12 month names and miles
  choice_of_user = ''
  for count in range(0, 12):
    months_collection.append(input("Please enter a month name:\n"))
    miles_collection.append(int(input("Please enter miles driven for the month:\n")))

def initialize_search(name_of_month_to_search_for):
  # find month and print its miles (returns 1 if found, else -1)
  found = -1
  for count in range(0, 12):
    if name_of_month_to_search_for == collection_of_months[count]:
      print("The month name is: " + name_of_month_to_search_for +
            " and the miles driven for the month is: " +
            str(collection_of_miles[count]))
      found = 1
  return found

def collection_of_miles_compared():
  # print smallest miles and its month (per given logic)
  smallest_miles = collection_of_miles[0]
  smallest_month = collection_of_months[0]
  for count in range(0, 12):
    if collection_of_miles[count] < collection_of_miles[0]:
      smallest_miles = collection_of_miles[count]
      smallest_month = collection_of_months[count]
  print("The result for searching the smallest miles:")
  print("The month name is: " + smallest_month +
        " and the miles driven for the month is: " + str(smallest_miles))

def collection_of_miles_compared_large():
  # print largest miles and its month
  largest_miles = collection_of_miles[0]
  largest_month = collection_of_months[0]
  for count in range(0, 12):
    if collection_of_miles[count] > largest_miles:
      largest_miles = collection_of_miles[count]
      largest_month = collection_of_months[count]
  print("The result for searching the largest miles:")
  print("The month name is: " + largest_month +
        " and the miles driven for the month is: " + str(largest_miles))

def list_of_options(choice_of_user):
  # menu loop
  while choice_of_user != "E":
    print("**** MENU OPTIONS ****")
    choice_of_user = input(
      "Type P to populate miles and month name.\n"
      "Type S to search for Month\n"
      "Type M to search for Month name with smallest Miles\n"
      "Type L to search for Month Name with Largest Miles\n"
      "Type E to exit\n" + "Please enter your choice:\n")
    if choice_of_user == "P":
      populate_the_arrays(collection_of_months, collection_of_miles)
      choice_of_user = ''
    elif choice_of_user == "S":
      month_name_to_search_for = input("Please enter the month name to search:\n")
      found_month = initialize_search(month_name_to_search_for)
      if found_month < 0:
        print("The month name not found!")
      choice_of_user = ''
    elif choice_of_user == "M":
      collection_of_miles_compared()
      choice_of_user = ''
    elif choice_of_user == "L":
      collection_of_miles_compared_large()
      choice_of_user = ''
    elif choice_of_user == "E":
      print("Thank you for using the program.")
      print("Bye")
    else:
      print("Invalid choice. Please try again!")
  return choice_of_user

choice_of_user = list_of_options(choice_of_user)
