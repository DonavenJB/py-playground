#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Problem 9 - calorie and distance calculator with name and gender

CALORIE_RATE = 0.653

def calorie_calculator():
    while True:
        name = input("Enter your name or 0 = Quit: ")
        if name == "0":
            print("Good bye")
            break
        gender = input("Enter your gender (1=male, 2=female, 0=Quit): ")
        if gender == "0":
            print("Good bye")
            break
        if gender not in ("1", "2"):
            print("Invalid gender. Use 1 or 2.")
            continue
        title = "Mr." if gender == "1" else "Ms."
        person = f"{title} {name.capitalize()}"
        print(f"Welcome {person}!")
        choice = input("Calculate (1) calories burned or (2) distance to run? ")
        try:
            weight = float(input("Enter your weight in pounds: "))
            if choice == "1":
                dist = float(input("Enter distance run in miles: "))
                print(f"Congratulations {person}, you burned {CALORIE_RATE * weight * dist:.1f} calories!")
            elif choice == "2":
                cals = float(input("Enter calories you want to burn: "))
                print(f"{person}, you need to run {cals / (CALORIE_RATE * weight):.1f} miles to burn {cals:.1f} calories!")
        except ValueError:
            print("Please enter valid numbers.")

if __name__ == "__main__":
    calorie_calculator()