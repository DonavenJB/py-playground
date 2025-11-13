# Donaven Bruce
# CS 119 - Project 4 Program Two

runners = ["Mike", "Tina", "Jason", "Vicky", "Tammy"]
miles = []

print("--- Please enter the miles run for each runner ---")
for runner in runners:
    print(f"\n--- Entering miles for {runner} ---")
    week = []
    for day in range(1, 8):
        while True:
            try:
                m = float(input(f"  Day {day}: "))
                week.append(m)
                break
            except ValueError:
                print("  Error: Enter a number.")
    miles.append(week)

print("\n--- Marathon Training Log ---")
print(f"{'Name':<10}{'Day 1':>8}{'Day 2':>8}{'Day 3':>8}{'Day 4':>8}{'Day 5':>8}{'Day 6':>8}{'Day 7':>8}{'Average':>10}")
print("-" * 82)

for i in range(len(runners)):
    name = runners[i]
    week = miles[i]
    avg = sum(week) / 7
    print(f"{name:<10}", end="")
    for day_miles in week:
        print(f"{day_miles:8.2f}", end="")
    print(f"{avg:10.2f}")

print("\n--- Daily Statistics (All Runners) ---")
for day in range(7):
    day_total = sum(miles[r][day] for r in range(len(runners)))
    day_avg = day_total / len(runners)
    print(f"Day {day+1}: Total = {day_total:.2f}, Average = {day_avg:.2f}")

print("\nProgram complete. Have a great day!")