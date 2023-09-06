# Simple Calculator Application
import math


def GreaterThan(a,b):
    c = a>b
    return c

def LessThan(a,b):
    c = a<b
    return c

def EqualTo(a,b):
    c = a==b
    return c

def NotEqualTo(a,b):
    c = a!=b
    return c

def GreaterOrEqual(a,b):
    c = a>=b
    return c

def LessOrEqual(a,b):
    c = a<=b
    return c


def LogicalOperationMenu():
    print("Start Simple Calculator Application")
    print("")
    print("|==============================|")
    print("| Menu:                        |")
    print("|==============================|")
    print("| 1. Greater than              |")
    print("| 2. Less than                 |")
    print("| 3. Equal to                  |")
    print("| 4. Not equal to              |")
    print("| 5. Greater than or equal to  |")
    print("| 6. Less than or equal to     |")
    print("| 7. Inverse                   |")
    print("| -1: Quit                     |")
    print("| =============================|")


def GetLogicalOperationMenuChoice():
    choice = 1
    while choice > 0:
        LogicalOperationMenu()
        choice = int(input("Enter Operation: "))
        if (choice == -1):
            break
    
        if ((choice > 7) or (choice < -1)):
            print("ERROR: Invalid Choice of Operation")
            print("Please Try again")
            choice = 1
            continue
    
        operand1 = int(input("Enter First Operand: "))
        if (choice <= 6):
            operand2 = int(input("Enter Second Operand: "))
        PrintOutput(choice, operand1, operand2)


def PrintOutput(choice, operand1, operand2=0):  #Operand2 has a default value of 0
    if choice == 1:
        print(operand1, '>', operand2, '=', GreaterThan(operand1,operand2))
    elif choice == 2:
        print(operand1, '<', operand2, '=', LessThan(operand1,operand2))
    elif choice == 3:
        print(operand1, '==', operand2, '=', EqualTo(operand1,operand2))
    elif choice == 4:
        print(operand1, '!=', operand2, '=', NotEqualTo(operand1,operand2))
    elif choice == 5:
        print(operand1, '>=', operand2, '=', GreaterOrEqual(operand1,operand2))
    elif choice == 6:
        print(operand1, '<=', operand2, '=', LessOrEqual(operand1,operand2))

    elif choice == 7:
        if operand1 == 0:
            print("ERROR: Divided by ZERO ERROR")
            print("please try again")
        else:
            print('1/', operand1, '=', CalcInverseOfX(operand1))
    else:
        pass # Break out of the while loop

if __name__ == '__main__':
    GetLogicalOperationMenuChoice()
    print("End Program: Have a good day")
    print("")


