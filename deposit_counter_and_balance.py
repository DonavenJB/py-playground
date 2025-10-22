"""
Program: Deposit Range Counter & Balance (7 Deposits)
Author: Donaven Bruce
Description: Prompts for 7 deposit amounts. Tracks how many deposits fall into
four ranges (>=1000, 500–999, 100–499, <100), rejects negatives, and prints
each count plus the final balance.
"""

# counters for each deposit range
deposits_ge_1000 = 0
deposits_500_999 = 0
deposits_100_499 = 0
deposits_lt_100 = 0

# running balance
current_balance = 0

# collect 7 deposits
for i in range(1, 8):
    deposit_amount = int(input("Please enter your deposit amount: \n"))

    # negative amounts are invalid
    if deposit_amount < 0:
        print("You entered a wrong amount!")
    else:
        # update balance
        current_balance = current_balance + deposit_amount

        # update range counters
        if deposit_amount >= 1000:
            deposits_ge_1000 = deposits_ge_1000 + 1
        elif 500 <= deposit_amount < 1000:
            deposits_500_999 = deposits_500_999 + 1
        elif 100 <= deposit_amount < 500:
            deposits_100_499 = deposits_100_499 + 1
        else:
            deposits_lt_100 = deposits_lt_100 + 1

# summaries 
print("You have " + str(deposits_ge_1000) + " deposit over  or equal to 1000 dollars.")
print("You have " + str(deposits_500_999) + " deposit between 500 and 999 dollars.")
print("You have " + str(deposits_100_499) + " deposit between 100 and 499 dollars. ")
print("You have " + str(deposits_lt_100) + " deposit below 100 dollars.")
print("Your balance is : " + str(current_balance))
