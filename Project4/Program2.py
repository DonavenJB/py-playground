# Donaven Bruce
# CS 119
# Project 4 Program Two

# This program logs and analyzes weekly miles for a group of runners.
# It takes user input for 5 runners over 7 days and displays stats.

runners = ["Mike", "Tina", "Jason", "Vicky", "Tammy"] # Runner names
miles = [] # Empty list for all miles

def get_runner_data(): # Gets all user input
  print("--- Please enter the miles run for each runner ---")
  
  for runner in runners: # Loop for each runner
    print(f"\n--- Entering miles for {runner} ---")
    runner_week = [] # Temp list for one week
    
    for day in range(7): # Loop 7 times for 7 days
      while True: # Keep asking for a number
        try:
          day_miles = float(input(f"  Enter miles for Day {day + 1}: ")) # Get miles
          runner_week.append(day_miles) # Add miles to week
          break # Good input, exit loop
        except ValueError: # Bad input
          print("  Error: Invalid input. Please enter a number.")
          
    miles.append(runner_week) # Add this week to the main list

def display_results(): # Prints the big table
  print("\n--- Marathon Training Log ---")
  
  # Print the table header
  print(f"{'Name':<10} {'Day 1':>8} {'Day 2':>8} {'Day 3':>8} {'Day 4':>8} {'Day 5':>8} {'Day 6':>8} {'Day 7':>8} {'Average':>10}")
  print("=" * 80) # Print a divider line
  
  for i in range(len(runners)): # Loop through each runner
    name = runners[i] # Get name
    runner_miles = miles[i] # Get miles
    
    total = sum(runner_miles) # Add up miles
    average = total / 7 # Get average
    
    print(f"{name:<10}", end="") # Print name
    
    for mile in runner_miles: # Loop through the 7 miles
      print(f"{mile:8.2f}", end="") # Print one mile
      
    print(f"{average:10.2f}") # Print average

def calculate_daily_stats(): # Prints daily totals and averages
  print("\n--- Daily Statistics (All Runners) ---")
  
  for j in range(7): # Loop through 7 days
    day_total = 0 # Reset total for this day
    
    for i in range(len(runners)): # Loop through 5 runners
      day_total += miles[i][j] # Add this runner's miles for this day
      
    day_average = day_total / len(runners) # Get this day's average
    
    print(f"Day {j + 1}: Total Miles = {day_total:.2f}, Average Miles = {day_average:.2f}")

def main(): # Controls the program
  get_runner_data() # Fill the lists
  display_results() # Print the table
  calculate_daily_stats() # Print daily stats
  print("\nProgram complete. Have a great day!")

main() # Runs the program