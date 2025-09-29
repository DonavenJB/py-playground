# Donaven Bruce
# Program 1: My program collects the Name, Amount of Lunch Menu item, and Amount of drink.
#            I calculate and output the Name and the Amount of each person's check including a 10% tax.
#            Next I calculate the total amount for all three together including a 20% tip.
#            Tips are calculated on the pre-tax group total (not on the taxed total).

tax_rate = 0.10
tip_rate = 0.20

# Initialize per-person amounts
amt_lunch_menu_1 = 0.00
amt_lunch_menu_2 = 0.00
amt_lunch_menu_3 = 0.00
amt_of_drink_1 = 0.00
amt_of_drink_2 = 0.00
amt_of_drink_3 = 0.00

pre_tax_total_1 = 0.00
pre_tax_total_2 = 0.00
pre_tax_total_3 = 0.00

# Getting user data for first person
user_name_1 = input("what is your name:\n")
amt_lunch_menu_1 = float(input("What is amount of lunch menu item:\n"))  # cast input to float
amt_of_drink_1 = float(input("what is amount of drink:\n"))              # cast input to float
pre_tax_total_1 = amt_lunch_menu_1 + amt_of_drink_1                      # sum the amount for both items

# Getting user data for second person
user_name_2 = input("what is your name:\n")
amt_lunch_menu_2 = float(input("What is amount of lunch menu item:\n"))  # cast input to float
amt_of_drink_2 = float(input("what is amount of drink:\n"))              # cast input to float
pre_tax_total_2 = amt_lunch_menu_2 + amt_of_drink_2                      # sum the amount for both items

# Getting user data for third person
user_name_3 = input("what is your name:\n")
amt_lunch_menu_3 = float(input("What is amount of lunch menu item:\n"))  # cast input to float
amt_of_drink_3 = float(input("what is amount of drink:\n"))              # cast input to float
pre_tax_total_3 = amt_lunch_menu_3 + amt_of_drink_3                      # sum the amount for both items

# Per-person totals with tax (no tip per person)
person_1_total = pre_tax_total_1 * (1 + tax_rate)
person_2_total = pre_tax_total_2 * (1 + tax_rate)
person_3_total = pre_tax_total_3 * (1 + tax_rate)

print(f"{user_name_1} ${person_1_total:.2f}")
print(f"{user_name_2} ${person_2_total:.2f}")
print(f"{user_name_3} ${person_3_total:.2f}")

# Group totals:
group_subtotal = pre_tax_total_1 + pre_tax_total_2 + pre_tax_total_3     # pre-tax group total
group_tax = group_subtotal * tax_rate
group_tip = group_subtotal * tip_rate                                    # tip on pre-tax group total
all_three_total = group_subtotal + group_tax + group_tip

# Output group total (includes tax + tip + base cost)
print(f"Total amount for all three ${all_three_total:.2f}")
