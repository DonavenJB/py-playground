def userInputValidation(option,string):
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


def optionOne():
    print("Placeholder: optionOne() was called")


def optionTwo():
    print("Placeholder: optionTwo() was called")


def optionThree():
    print("Placeholder: optionThree() was called")


def optionFour():
    print("Placeholder: optionFour() was called")


def optionFive():
    print("Placeholder: optionFive() was called")


def optionSix():
    print("Placeholder: optionSix() was called")


def optionSeven():
    print("Placeholder: optionSeven() was called")


def main():
    option =1
    while option != 8:
        string = "1- Run option one .................optionOne()\n" \
                 "2- Run option two .................optionTwo()\n" \
                 "3- Run option three ...............optionThree()\n" \
                 "4- Run option four ................optionFour()\n" \
                 "5- Run option five ................optionFive()\n" \
                 "6- Run option six .................optionSix()\n" \
                 "7- Run option seven ...............optionSeven()\n" \
                 "8- Quit the program ...............exit()\n" \
                 "Please enter the option:"

        option = userInputValidation(option,string)

        if option == 1:
            optionOne()
        elif option == 2:
            optionTwo()
        elif option == 3:
            optionThree()
        elif option == 4:
            optionFour()
        elif option == 5:
            optionFive()
        elif option == 6:
            optionSix()
        elif option == 7:
            optionSeven()
        elif option == 8:
            exit()

main()
