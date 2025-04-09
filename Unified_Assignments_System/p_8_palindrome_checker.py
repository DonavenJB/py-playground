#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci


# Problem 8 - palindrome checker with file save and test function

def test_palindrome(s):
    return 1 if s == s[::-1] else 0

def palindrome_checker():
    s = input("Please enter a string for Palindrome status: ")
    rev = s[::-1]
    print("You entered")
    print(s)
    print("Your word reversed is :")
    print(rev)
    with open("palindrome_check.txt", "w") as f:
        f.write(f"Original String: {s}\n")
        f.write(f"Reversed String: {rev}\n")           # save both versions
    print("Strings saved to palindrome_check.txt")
    if test_palindrome(s):                              # use required function
        print("Yes, you entered a Palindrome")
    else:
        print("No, your word is NOT a Palindrome")

if __name__ == "__main__":
    palindrome_checker()