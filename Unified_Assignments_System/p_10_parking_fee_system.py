#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Problem 10 - parking fee system with table and total charge
import math

def parking_fee(hours):
    if hours >= 24 or hours < 0: return 12.00
    if hours <= 1: return 3.00
    extra = math.ceil(hours - 1)                       # charge per extra hour or part
    return min(3.00 + extra, 12.00)                    # cap at maximum

def parking_system():
    try:
        n = int(input("Please enter number of customers: "))
        if n <= 0:
            print("No customers to process.")
            return
        total = 0.0
        print(f"{'Customer #':<12} {'Hours parked':<12} {'Total':>8}")
        for i in range(1, n + 1):
            h = float(input(f"Customer {i} - hours parked: "))
            charge = parking_fee(h)
            total += charge
            print(f"{i:<12} {h:<12.1f} ${charge:>7.1f}")
        print(f"\nTotal charge for {n} customers = ${total:.1f}")
        print("#" * 50)
    except ValueError:
        print("Invalid input. Enter valid numbers.")

if __name__ == "__main__":
    parking_system()