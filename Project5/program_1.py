# Donaven Bruce
# My program calculates a patient’s total hospital charges by asking if they are in-patient or out-patient, 
# validating all inputs, and then computing the bill from days, daily rate, services, and medication costs.

def userInputValidation(option,string):
    # Validate menu option input
    while True:
        try:
            option = int(input(string))
            while option < 1 or option > 3:
                print("option should be >=1 or <= 3")
                option = int(input(string))
            break
        except:
            print("Invalid entry")
    return option


def validateNonNegative(prompt):
    # Ensure user enters a non negative number
    while True:
        try:
            value = float(input(prompt))
            # Repeat until value is zero or greater
            while value < 0:
                print("Value cannot be negative")
                value = float(input(prompt))
            break
        except:
            print("Invalid entry")
    return value


def calcInPatientTotal(days,dailyRate,serviceCharges,medCharges):
    # Compute total charges for in patient
    total = days * dailyRate + serviceCharges + medCharges
    return total


def calcOutPatientTotal(serviceCharges,medCharges):
    # Compute total charges for out patient
    total = serviceCharges + medCharges
    return total


def processInPatient():
    # Get all values for in patient billing
    days = int(validateNonNegative("Enter number of days spent in the hospital: "))
    # Store number of days as an integer
    dailyRate = validateNonNegative("Enter the daily rate: ")
    serviceCharges = validateNonNegative("Enter charges for hospital services: ")
    medCharges = validateNonNegative("Enter hospital medication charges: ")
    total = calcInPatientTotal(days,dailyRate,serviceCharges,medCharges)
    print("Total in-patient charges are: {:.2f}".format(total))


def processOutPatient():
    # Get all values for out patient billing
    serviceCharges = validateNonNegative("Enter charges for hospital services: ")
    medCharges = validateNonNegative("Enter hospital medication charges: ")
    total = calcOutPatientTotal(serviceCharges,medCharges)
    print("Total out-patient charges are: {:.2f}".format(total))


def main():
    # Control program menu and user choice
    option =1
    while option != 3:
        string = "1- Process in-patient charges ........processInPatient()\n" \
                 "2- Process out-patient charges .......processOutPatient()\n" \
                 "3- Quit the program ..................exit()\n" \
                 "Please enter the option:"

        option = userInputValidation(option,string)

        if option == 1:
            processInPatient()
        elif option == 2:
            processOutPatient()
        elif option == 3:
            exit()

main()
