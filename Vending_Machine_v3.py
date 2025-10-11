# Donaven Bruce
# Coffee Vending Machine – Program 3: drink selector menu
# My program displays at least 4 drink options with their prices (Small, Medium = 2x, Large = 3x)
# The user enters the option number for the drink they want
# If the option is invalid my program prints an error and exits
# My program records the small drink price into a variable for the next program
# Finally I print a confirmation to the user

POS_PREFIX = "  $"
LABEL_W = 25
VALUE_W = 6

# prices
small_price  = 1.75
medium_price = round(small_price * 2, 2)
large_price  = round(small_price * 3, 2)

# drink names
d1 = "Espresso"
d2 = "Americano"
d3 = "Café au Lait"
d4 = "Latte"
d5 = "Cappuccino"
d6 = "Macchiato"
d7 = "Mocha"

print("***** Coffee Vending Machine *****\n")
print(f"{'MENU':^50}")

# show menu 
print(f"1. {d1} (Small ${small_price:.2f} , Medium ${medium_price:.2f}, Large ${large_price:.2f})")
print(f"2. {d2} (Small ${small_price:.2f} , Medium ${medium_price:.2f}, Large ${large_price:.2f})")
print(f"3. {d3} (Small ${small_price:.2f} , Medium ${medium_price:.2f}, Large ${large_price:.2f})")
print(f"4. {d4} (Small ${small_price:.2f} , Medium ${medium_price:.2f}, Large ${large_price:.2f})")
print(f"5. {d5} (Small ${small_price:.2f} , Medium ${medium_price:.2f}, Large ${large_price:.2f})")
print(f"6. {d6} (Small ${small_price:.2f} , Medium ${medium_price:.2f}, Large ${large_price:.2f})")
print(f"7. {d7} (Small ${small_price:.2f} , Medium ${medium_price:.2f}, Large ${large_price:.2f})")

# get selection
choice = input("\nEnter drink option (1-7): ").strip()

# conditional selection
if choice == "1":
    drink = d1
elif choice == "2":
    drink = d2
elif choice == "3":
    drink = d3
elif choice == "4":
    drink = d4
elif choice == "5":
    drink = d5
elif choice == "6":
    drink = d6
elif choice == "7":
    drink = d7
else:
    print("Error: Invalid drink option")
    raise SystemExit()

# record small price for next program and display it now
amount_due_small = small_price

print(f"\nYou selected {drink}.")
print(f"{'Amount due (small)':<{LABEL_W}}{(POS_PREFIX + f'{amount_due_small:.2f}'):>{VALUE_W + len(POS_PREFIX)}}")
