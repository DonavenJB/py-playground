# Donaven Bruce
# Coffee Vending Machine – Money collection interface
# My program displays the title and item price before accepting user payment
# As required I have ensured to account for both dollars and cents 
# After gathering the required input, My program checks 
# - If payment < price: print message and exit
# - If payment >= price: compute change; print only if non-zero
# Finally my program will Print thank you message on successful sale
#The spec allows assuming digits only

POS_PREFIX = "  $"
LABEL_W = 25
VALUE_W = 6

# Prices
coffee_price_small = 1.25

print("***** Coffee Vending Machine *****")
print(f"{'MENU':^33}")
print(f"{'Small (9oz) Coffee':<{LABEL_W}}{(POS_PREFIX + f'{coffee_price_small:.2f}'):>{VALUE_W + len(POS_PREFIX)}}")

print("\nPlease insert funds below")
str_credit = input("$")
credit = float(str_credit)

if credit < coffee_price_small:
    print("Insufficient funds, no sale!")
    raise SystemExit()

balance = credit - coffee_price_small
# Print change 
if abs(balance) >= 0.005:
    print(f"{'Please take your change':<{LABEL_W}}{(POS_PREFIX + f'{balance:.2f}'):>{VALUE_W + len(POS_PREFIX)}}")

print("Thank You!")
print("Enjoy your coffee - Goodbye!")
