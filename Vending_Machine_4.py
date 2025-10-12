# Donaven Bruce
# Coffee Vending Machine – Program 4
# My program shows the drink menu, asks for a drink choice and records the small price.
# Then it shows size options, records the size and a price multiplier.
# It computes the total due, asks for payment, and returns change as needed.
# I’m using simple floats with a tiny epsilon for comparisons.

POS_PREFIX = "  $"
LABEL_W = 25
VALUE_W = 6

# base prices
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

# get drink selection
choice = input("\nEnter drink option (1-7): ").strip()

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

# record amount due for a small
amount_due_small = small_price
print(f"\nYou selected {drink}.")
print(f"{'Amount due (small)':<{LABEL_W}}{(POS_PREFIX + f'{amount_due_small:.2f}'):>{VALUE_W + len(POS_PREFIX)}}")

# size selection
s = input("\nEnter size (s=small, m=medium, l=large): ").strip()
if s in ("s", "S"):
    size, multiplier = "small", 1
elif s in ("m", "M"):
    size, multiplier = "medium", 2
elif s in ("l", "L"):
    size, multiplier = "large", 3
else:
    print("Error: Invalid drink size")
    raise SystemExit()

print(f"You have ordered a {size} drink.")
print(f"Price multiplier: {multiplier}")

# compute total due from small price and multiplier
selected_price = amount_due_small * multiplier
print(f"\n{'Total due':<{LABEL_W}}{(POS_PREFIX + f'{selected_price:.2f}'):>{VALUE_W + len(POS_PREFIX)}}")

# payment + change logic 
str_credit = input("\nPlease insert payment\n$").strip()
# spec allows assuming digits only so simple parse
credit = float(str_credit)

# float safe comparison with tiny epsilon
if credit + 1e-9 < selected_price:
    print("Insufficient funds, no sale!")
    raise SystemExit()

balance = credit - selected_price
if abs(balance) >= 0.005:
    print(f"{'Please take your change':<{LABEL_W}}{(POS_PREFIX + f'{balance:.2f}'):>{VALUE_W + len(POS_PREFIX)}}")

print("Thank you – enjoy your coffee!")
