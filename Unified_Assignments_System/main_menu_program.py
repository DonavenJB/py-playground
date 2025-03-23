#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

import p_1_star_rows
import p_2_triangle_pattern
import p_3_number_patterns
import p_4_heads_or_tails_game as g4
import p_5_guess_the_number as g5
import p_6_multiplication_table
import p_7_file_sort_words
import p_8_palindrome_checker
import p_9_calorie_distance_calc
import p_10_parking_fee_system


def guessing_games():
    while True:
        print("\nSelect guessing game:")
        print("1. Heads or Tails")
        print("2. Guess the Number (1-10)")
        print("0. Back to main menu")
        ch = input("Enter choice (0-2): ")
        if ch == "1":
            g4.coin_flip_game()
        elif ch == "2":
            g5.guess_the_number()
        elif ch == "0":
            break


while True:
    print("\nSelect operation.")
    print("1. Star Rows Pattern")
    print("2. Star Diamond Pattern")
    print("3. Number Pyramids")
    print("4. Multiplication Table")
    print("5. Guessing Games")
    print("6. Sort Words & Save")
    print("7. Palindrome Checker")
    print("8. Calorie Calculator")
    print("9. Parking Fee System")
    print("0. Exit")
    
    choice = input("Enter choice(0-9): ").strip()
    
    if choice == "1":
        p_1_star_rows.print_star_rows()
    elif choice == "2":
        p_2_triangle_pattern.print_star_diamond()
    elif choice == "3":
        p_3_number_patterns.print_number_pyramid()
    elif choice == "4":
        p_6_multiplication_table.multiplication_table()
    elif choice == "5":
        guessing_games()
    elif choice == "6":
        p_7_file_sort_words.save_and_sort_words()
    elif choice == "7":
        p_8_palindrome_checker.palindrome_checker()
    elif choice == "8":
        p_9_calorie_distance_calc.calorie_calculator()
    elif choice == "9":
        p_10_parking_fee_system.parking_system()
    elif choice == "0":
        print("Goodbye")
        break
    else:
        print("Invalid choice!")