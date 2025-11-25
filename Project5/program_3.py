# Donaven Bruce
# This program displays a menu to manage a list of student names by letting the user add, 
# remove, insert, find the maximum and minimum, sort the list in descending order, 
# and display the list using only len and index as helpers.


# Global list of student names
studentFullName = ["Mike navarro","Miguel saba","Maria Rami"]

def userInputValidation(option,string):
    # Validate menu option input
    while True:
        try:
            option = int(input(string))
            while option < 1 or option > 8:
                print("option should be >=1 or <= 8")
                option = int(input(string))
            break
        except:
            print("Invalid entry")
    return option


def addItem():
    global studentFullName
    # Show list before adding item
    print("Original list:", studentFullName)
    item = input("Please enter the value for the item you want to add: ")
    # Add new name to end of list
    studentFullName = studentFullName + [item]
    print("List after adding an item:", studentFullName)


def removeItem():
    global studentFullName
    # Show list before attempting remove
    print("Original list:", studentFullName)
    item = input("Please enter the value for the item you want to remove: ")
    try:
        # Remove first match of given name
        idx = studentFullName.index(item)
        studentFullName = studentFullName[:idx] + studentFullName[idx+1:]
        print("List after removing the item:", studentFullName)
    except:
        # Handle case when name is not found
        print("Item not found. List unchanged:", studentFullName)


def insertToList():
    global studentFullName
    # Show list before insert
    print("Original list:", studentFullName)
    try:
        index = int(input("Where do you want to insert the item? Enter the index number: "))
        # Check and validate insert index
        while index < 0 or index > len(studentFullName):
            print("Index should be between 0 and", len(studentFullName))
            index = int(input("Where do you want to insert the item? Enter the index number: "))
    except:
        print("Invalid index entry")
    # Insert new name at given index
        return
    item = input("Please enter the value for the item you want to insert: ")
    studentFullName = studentFullName[:index] + [item] + studentFullName[index:]
    print("List after inserting an item into index", index, ":", studentFullName)


def findMax():
    global studentFullName
    if len(studentFullName) == 0:
        print("List is empty")
        return
    print("Current list:", studentFullName)
    # Find largest name value
    maximum = studentFullName[0]
    i = 1
    while i < len(studentFullName):
        if studentFullName[i] > maximum:
            maximum = studentFullName[i]
        i = i + 1
    print("Maximum value in the list is:", maximum)
    print("List after operation unchanged:", studentFullName)


def findMin():
    global studentFullName
    if len(studentFullName) == 0:
        print("List is empty")
        return
    print("Current list:", studentFullName)
    # Find smallest name value
    minimum = studentFullName[0]
    i = 1
    while i < len(studentFullName):
        if studentFullName[i] < minimum:
            minimum = studentFullName[i]
        i = i + 1
    print("Minimum value in the list is:", minimum)
    print("List after operation unchanged:", studentFullName)


def sortList():
    global studentFullName
    # Sort names in descending order
    print("Original list:", studentFullName)
    n = len(studentFullName)
    i = 0
    while i < n - 1:
        maxIndex = i
        j = i + 1
        while j < n:
            if studentFullName[j] > studentFullName[maxIndex]:
                maxIndex = j
            j = j + 1
        if maxIndex != i:
            temp = studentFullName[i]
            studentFullName[i] = studentFullName[maxIndex]
            studentFullName[maxIndex] = temp
        i = i + 1
    print("List after sorting in descending order:", studentFullName)


def displayList():
    global studentFullName
    # Display current list contents
    print("Current list:", studentFullName)


def main():
    # Main menu control loop
    option = 1
    while option != 8:
        string = "1- Add an item to the list  ..........addItem(item)\n" \
                 "2- Remove item from the list .......removeItem(item)\n" \
                 "3- Insert an item to the list .....insertToList(item, index)\n" \
                 "4- Find maximum ....findMax(list)\n" \
                 "5- Find Minimum ....findMin(list)\n" \
                 "6- Sort the list in descending order .....sortList(list)\n" \
                 "7- Display the list.... displayList(list)\n" \
                 "8- Quit the program .....exit()\n" \
                 "Please enter your option: "

        option = userInputValidation(option,string)

        if option == 1:
            addItem()
        elif option == 2:
            removeItem()
        elif option == 3:
            insertToList()
        elif option == 4:
            findMax()
        elif option == 5:
            findMin()
        elif option == 6:
            sortList()
        elif option == 7:
            displayList()
        elif option == 8:
            exit()

main()
