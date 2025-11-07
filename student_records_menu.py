"""
Program: Student Records Menu (Populate/Update/Display/Grade)
Author: Donaven Bruce
Description: Manages 4 students. Menu to populate name/ID/3 scores, update a
student's scores, display a student's info by ID, and compute average + letter
grade by ID.
"""

# user choice and parallel arrays
user_choice = ''
student_names = []
student_ids = []
scores1 = []
scores2 = []
scores3 = []

def populate_the_array():
  # read 4 students: name, ID, and 3 scores
  for count in range(0, 4):
    student_names.append(input("Please enter a student's name :\n"))
    student_ids.append(int(input("Please enter the student's ID:\n")))
    scores1.append(int(input("Please enter first score:\n")))
    scores2.append(int(input("Please enter scond score:\n")))
    scores3.append(int(input("Please enter third score:\n")))

def initialize_disciple_grade_calculator():
  # find by ID, print average and letter grade
  found = -1
  disciple_id_num = int(input("Please enter the ID of the student:\n"))
  for count in range(0, 4):
    if disciple_id_num == student_ids[count]:
      found = 1
      disciple_mean_of_scores = ((scores1[count] + scores2[count] + scores3[count])) / 3
      print("The average is: " + str(disciple_mean_of_scores))
      if disciple_mean_of_scores >= 90:
        print("The grade is: A")
      elif disciple_mean_of_scores <= 89 and disciple_mean_of_scores >= 80:
        print("The grade is: B")
      elif disciple_mean_of_scores <= 79 and disciple_mean_of_scores >= 70:
        print("The grade is: C")
      elif disciple_mean_of_scores <= 69 and disciple_mean_of_scores >= 60:
        print("The grade is: D")
      else:
        print("The grade is: F")
  return found

def initiate_update_disciple_info():
  # find by ID, show current info, then update 3 scores
  disciple_id_num = int(input("Please enter the ID of the student:\n"))
  found = -1
  for count in range(0, 4):
    if disciple_id_num == student_ids[count]:
      found = 1
      print("The student name is: " + student_names[count] +
            "\nID is: " + str(student_ids[count]) +
            "\nFirst score  is: " + str(scores1[count]) +
            "\nSecond score  is: " + str(scores2[count]) +
            "\nThird score  is: " + str(scores3[count]))
      scores1[count] = int(input("Please enter first score:\n"))
      scores2[count] = int(input("Please enter scond score:\n"))
      scores3[count] = int(input("Please enter third score:\n"))
  return found

def display_disciple_information():
  # find by ID and print all fields
  disciple_id_num = int(input("Please enter the ID of the student:\n")) 
  found = -1
  for count in range(0, 4):
    if disciple_id_num == student_ids[count]:
      found = 1
      print("The student name is: " + student_names[count] +
            "\nID is: " + str(student_ids[count]) +
            "\nFirst score  is: " + str(scores1[count]) +
            "\nSecond score  is: " + str(scores2[count]) +
            "\nThird score  is: " + str(scores3[count]))
  return found  

def list_of_options(user_choice_passed):
  # main menu loop
  while user_choice_passed != "E":
    print("**** MENU OPTIONS ****")
    user_choice_passed = input(
      "Type P to populate the student information.\n"
      "Type U to update student Information\n"
      "Type D to display the student information.\n"
      "Type C to calculate the Grade.\n"
      "Type E to exit\n"
      "Please enter your choice:\n")
    if user_choice_passed == "P":
      populate_the_array()
      user_choice_passed = ''
    elif user_choice_passed == "U":
      search_result_id = initiate_update_disciple_info()
      if search_result_id < 0:
        print("The ID is not found!")
    elif user_choice_passed == "D":
      disciple_id_search_result = display_disciple_information()
      if disciple_id_search_result < 0:
        print("The ID is not found!")
    elif user_choice_passed == "C":
      id_search_result = initialize_disciple_grade_calculator()
      if id_search_result < 0:
        print("The ID is not found!")
    elif user_choice_passed == "E":
      print("Thank you for using the program.\n" + "Bye")
    else:
      print("Invalid choice. Please try again!")
  return user_choice_passed

# start menu
list_of_options(user_choice)
