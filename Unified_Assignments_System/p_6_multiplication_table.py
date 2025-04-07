#Student: Donaven Bruce

#Instructor: Kaleab Gorfu

#CS 119 : Intro to Comp Sci

# Problem 6 - multiplication table with border lines

def multiplication_table():
    table = int(input("Enter multiplication table you want to see "))
    max_num = int(input("Enter max you want your table to go "))
    print("---------------------")
    print(f"The table of {table}")
    print("---------------------")
    for i in range(1, max_num + 1):
        print(f"{i} * {table} = {i * table}")           # print each line
    print("---------------------")
    print("Done counting...")
    print("---------------------")

if __name__ == "__main__":
    multiplication_table()