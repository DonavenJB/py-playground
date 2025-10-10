# Donaven Bruce
# Coffee Vending Machine – Drink size selector 
# My program shows the three sizes and asks the user for s/m/l (case-insensitive).
# After input, I print which size was chosen and record the price multiplier:
# - small = 1, medium = 2, large = 3
# If the user enters anything else, I print an error and exit.
# At the end I print the multiplier so it can be used in the later program.


POS_PREFIX = "  $"
LABEL_W = 25
VALUE_W = 6

# Prices
coffee_price_small = 1.25
coffee_price_medium = coffee_price_small * 2
coffee_price_large = coffee_price_small * 3

print("***** Coffee Vending Machine *****")
print(f"{'MENU':^33}")
print(f"{'Small (9oz) Coffee':<{LABEL_W}}{(POS_PREFIX + f'{coffee_price_small:.2f}'):>{VALUE_W + len(POS_PREFIX)}}")
print(f"{'Medium (12oz) Coffee':<{LABEL_W}}{(POS_PREFIX + f'{coffee_price_medium:.2f}'):>{VALUE_W + len(POS_PREFIX)}}")
print(f"{'Large (15oz) Coffee':<{LABEL_W}}{(POS_PREFIX + f'{coffee_price_large:.2f}'):>{VALUE_W + len(POS_PREFIX)}}")

s = input("Enter size (s/m/l): ").strip()
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

# Use selected size price 
selected_price = coffee_price_small * multiplier

print("\nPlease insert funds below")
str_credit = input("$")
credit = float(str_credit)

# Float safe comparison 
if credit + 1e-9 < selected_price:
    print("Insufficient funds, no sale!")
    raise SystemExit()

balance = credit - selected_price
# Print change only if non-zero 
if abs(balance) >= 0.005:
    print(f"{'Please take your change':<{LABEL_W}}{(POS_PREFIX + f'{balance:.2f}'):>{VALUE_W + len(POS_PREFIX)}}")

print("Thank You!")
print("Enjoy your coffee - Goodbye!")
