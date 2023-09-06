# Simple Calculator Application
import calculator_arthimitic_operation_1
import calculator_converstion_operation_1
import calculator_logical_operation_1


def CalculatorMenu():
    print("Start Simple Calculator Application")
    print("")
    print("|==============================|")
    print("|        Main Menu             |")
    print("|==============================|")
    print("| 1. Arthemitic Operation      |")
    print("| 2. Logical Operation         |")
    print("| 3. Unit Conversion           |")
    print("| -1: Quit                     |")
    print("| =============================|")
    
def GetCalculatorMenuChoice():
    choice = 1
    while choice > 0:
        CalculatorMenu()
        choice = int(input("Enter Operation: "))
        if (choice == -1):
            break

        if ((choice > 4) or (choice < -1)):
            print("ERROR: Invalid Choice of Operation")
            print("Please Try again")
            choice = 1
            continue
        
        SelectCalculatorMenu(choice)


def SelectCalculatorMenu(choice):
    if choice == 1:
        calculator_arthimitic_operation_1.GetArithemiticMenu()
    elif choice == 2:
        calculator_logical_operation_1.GetLogicalOperationMenuChoice()
    elif choice == 3:
        calculator_converstion_operation_1.GetConversionMenuChoice()
    else:
        pass # Break out


if __name__ == '__main__':
    GetCalculatorMenuChoice()
    print("End Program: Have a good day")
    print("")
