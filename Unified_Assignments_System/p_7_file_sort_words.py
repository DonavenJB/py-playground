#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Problem 7 - save words to file then sort and append

def save_and_sort_words():
    words = input("Please provide a few words separated by spaces: ")
    print(f"You entered the words below:\n{words}")
    with open("word_output.txt", "w") as f:
        f.write("Original Words:\n" + words + "\n\n")   # save original
    sorted_words = sorted(words.split())
    print("\nThe sorted words are:")
    for w in sorted_words:
        print(w)
    with open("word_output.txt", "a") as f:
        f.write("Sorted Words (Alphabetical):\n")
        for w in sorted_words:
            f.write(w + "\n")                           # append sorted list
    print("\nSorted words appended to word_output.txt")

if __name__ == "__main__":
    save_and_sort_words()