# Program 3: Cellular Telephone Bill
# Donaven Bruce
# My Program gets each student's name and three scores, computes average, and assigns a letter grade.
# Validates inputs and prints name, average, and grade.

print("*** Cellular Telephone Bill ***")

while True:
    # account number non-empty
    account = input("Enter account number: ").strip()
    while account == "":
        account = input("Account number cannot be empty. Enter account number: ").strip()

    # service code choiceas R or P
    code = input("Enter service code (R for Regular, P for Premium): ").strip().upper()
    while code not in ("R", "P"):
        code = input("Invalid. Enter service code (R or P): ").strip().upper()

    if code == "R":
        # total minutes >= 0
        while True:
            raw_total = input("Enter total minutes used: ").strip()
            try:
                total_minutes = float(raw_total)
                if total_minutes < 0:
                    continue
                break
            except ValueError:
                pass

        over = max(0, total_minutes - 50)
        amount_due = 10.00 + over * 0.20

        print("\n--- BILL SUMMARY ---")
        print("Account number:", account)
        print("Service type:   Regular")
        print("Total minutes:  ", format(total_minutes, ".2f"))
        print("Amount due:     $", format(amount_due, ".2f"), sep="")
        print("--------------------\n")

    else:
        # day minutes >= 0
        while True:
            raw_day = input("Enter DAY minutes (6:00 a.m. to 6:00 p.m.): ").strip()
            try:
                day_minutes = float(raw_day)
                if day_minutes < 0:
                    continue
                break
            except ValueError:
                pass

        # night minutes >= 0
        while True:
            raw_night = input("Enter NIGHT minutes (6:00 p.m. to 6:00 a.m.): ").strip()
            try:
                night_minutes = float(raw_night)
                if night_minutes < 0:
                    continue
                break
            except ValueError:
                pass

        day_over = max(0, day_minutes - 75)
        night_over = max(0, night_minutes - 100)
        amount_due = 25.00 + day_over * 0.10 + night_over * 0.05

        print("\n--- BILL SUMMARY ---")
        print("Account number:", account)
        print("Service type:   Premium")
        print("Day minutes:    ", format(day_minutes, ".2f"))
        print("Night minutes:  ", format(night_minutes, ".2f"))
        print("Amount due:     $", format(amount_due, ".2f"), sep="")
        print("--------------------\n")

    # continue
    again = input("Continue? (YES to continue): ").strip().upper()
    if again != "YES":
        break

print("=== Done ===")
