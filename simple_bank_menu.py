"""
Program: Simple Banking Menu 
Author: Donaven Bruce
Description: Menu-driven deposit, withdraw, balance display, and exit.
Prompts repeatedly until the user chooses E. Prints "Not enough balance"
when a withdrawal would make the balance negative, and shows separators.
"""

# starting balance and loop control
balance = 0
user_choice = ""

# menu loop
while user_choice != "E":
  # menu prompt 
  user_choice = input("Type D to deposit money\n" +
  "Type W to withdraw money\n" +
  "Type B to display Balance\n" +
  "Type E to exit\n" + "Enter your choice now:\n")

  # deposit
  if user_choice == "D":
    deposit_amount = int(input("Please enter your amount to deposit:\n"))
    balance = balance + deposit_amount
    print("*****")

  # withdraw
  elif user_choice == "W":
    withdraw_amount = int(input("Please enter the amount you want to withdraw:\n"))
    if balance - withdraw_amount >= 0:
      balance = balance - withdraw_amount
    elif withdraw_amount > balance:
      print("Not enough balance")
    print("*****")

  # display balance
  elif user_choice == "B":
    print("Your balance is: " + str(balance))
    print("*****")

  # exit
  elif user_choice == "E":
    user_choice == "E"

  # invalid choice  
  elif user_choice != "E" or user_choice != "D" or user_choice != "B" or user_choice != "W":
    print("Invalid choice. Try again")
    print("*****")
