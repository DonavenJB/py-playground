#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Problem 4 - heads or tails game exit with zero
import random

def coin_flip_game():
    while True:
        choice = input("Guess Heads(1) Tails(2) Exit(0): ")
        if choice == "0":
            print("Goodbye")
            break
        if choice not in ("1", "2"):
            print("Invalid input. Enter 1, 2, or 0.")
            continue
        flip = random.randint(1, 2)
        result = "Heads" if flip == 1 else "Tails"
        print(f"The flip was {result}")
        print("You win" if int(choice) == flip else "You loose")  # check win

if __name__ == "__main__":
    coin_flip_game()