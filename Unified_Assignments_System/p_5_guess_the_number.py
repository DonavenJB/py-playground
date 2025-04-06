#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Problem 5 - guess number from 1 to 10 with try count
import random

def guess_the_number():
    secret = random.randint(1, 10)
    tries = 0
    while True:
        tries += 1
        try:
            guess = int(input("Guess any number 1 to 10:"))
        except ValueError:
            print("Please enter a valid number.")
            tries -= 1
            continue
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("You got it!")
            print(f"And it only took you {tries} tries!")   # show attempts
            break

if __name__ == "__main__":
    guess_the_number()