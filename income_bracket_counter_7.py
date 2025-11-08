"""
Program: Income Bracket Counter (7 People)
Author: Donaven Bruce
Description: Prompts for seven yearly incomes, counts how many fall into
four brackets (<=30000, 30001–50000, 50000–75000, >75000), and prints each
count plus the combined total income.
"""

# counters for each bracket
low_income_count = 0              # income <= 30000
mid_income_count = 0              # 30000 < income <= 50000
upper_mid_income_count = 0        # 50000 <= income <= 75000
high_income_count = 0             # income > 75000

# collect seven incomes
person1_income = int(input("Please enter yearly income of first person :\n"))
person2_income = int(input("Please enter yearly income of second person :\n"))
person3_income = int(input("Please enter yearly income of third person :\n"))
person4_income = int(input("Please enter yearly income of fourth person :\n"))
person5_income = int(input("Please enter yearly income of fifth person :\n"))
person6_income = int(input("Please enter yearly income of sixth person :\n"))
person7_income = int(input("Please enter yearly income of seventh person :\n"))

# bracket checks for person 1
if person1_income <= 30000:
  low_income_count = low_income_count + 1
elif person1_income > 30000 and person1_income <= 50000:
  mid_income_count = mid_income_count + 1
elif person1_income >= 50000 and person1_income <= 75000:
  upper_mid_income_count = upper_mid_income_count + 1
elif person1_income > 75000:
  high_income_count = high_income_count + 1

# bracket checks for person 2
if person2_income <= 30000:
  low_income_count = low_income_count + 1
elif person2_income > 30000 and person2_income <= 50000:
  mid_income_count = mid_income_count + 1
elif person2_income >= 50000 and person2_income <= 75000:
  upper_mid_income_count = upper_mid_income_count + 1
elif person2_income > 75000:
  high_income_count = high_income_count + 1

# bracket checks for person 3
if person3_income <= 30000:
  low_income_count = low_income_count + 1
elif person3_income > 30000 and person3_income <= 50000:
  mid_income_count = mid_income_count + 1
elif person3_income >= 50000 and person3_income <= 75000:
  upper_mid_income_count = upper_mid_income_count + 1
elif person3_income > 75000:
  high_income_count = high_income_count + 1

# bracket checks for person 4
if person4_income <= 30000:
  low_income_count = low_income_count + 1
elif person4_income > 30000 and person4_income <= 50000:
  mid_income_count = mid_income_count + 1
elif person4_income >= 50000 and person4_income <= 75000:
  upper_mid_income_count = upper_mid_income_count + 1
elif person4_income > 75000:
  high_income_count = high_income_count + 1

# bracket checks for person 5
if person5_income <= 30000:
  low_income_count = low_income_count + 1
elif person5_income > 30000 and  person5_income <= 50000:
  mid_income_count = mid_income_count + 1
elif person5_income >= 50000 and person5_income <= 75000:
  upper_mid_income_count = upper_mid_income_count + 1
elif person5_income > 75000:
  high_income_count = high_income_count + 1

# bracket checks for person 6
if person6_income <= 30000:
  low_income_count = low_income_count + 1
elif person6_income > 30000 and person6_income <= 50000:
  mid_income_count = mid_income_count + 1
elif person6_income >= 50000 and person6_income <= 75000:
  upper_mid_income_count = upper_mid_income_count + 1
elif person6_income > 75000:
  high_income_count = high_income_count + 1

# bracket checks for person 7
if person7_income <= 30000:
  low_income_count = low_income_count + 1
elif person7_income > 30000 and person7_income <= 50000:
  mid_income_count = mid_income_count + 1
elif person7_income >= 50000 and person7_income <= 75000:
  upper_mid_income_count = upper_mid_income_count + 1
elif person7_income > 75000:
  high_income_count = high_income_count + 1

# total income of all seven people
total_income_all_people = (person1_income + person2_income + person3_income + person4_income + person5_income + person6_income + person7_income)

# results
print("Number of people who made less than  or equal to 30000 is :" + str(low_income_count))
print("Number of people who made above 30000 and  less than or equal to 50000 is :" + str(mid_income_count))
print("Number of people who made  above 50000 and less than or equal to 75000 is :" + str(upper_mid_income_count))
print("Number of people who made  above 75000 is :" + str(high_income_count))
print("The total(Combined) earning made by all people is :" + str(total_income_all_people))
