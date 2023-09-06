# Simple Calculator Application
import math


def Addition(a,b):
    return a+b

def Subtraction(a,b):
    c = a-b
    return c

def Multiplication(a,b):
    c = a*b
    return c

def Division(a,b):
    c = a/b
    return c

def Modulus(a,b):
    c = a%b
    return c

def Floor(a,b):
    c = a//b
    return c

def Exponent(a,b):
    c = a**b
    return c

def CalcSquareOfX(x):
    return x**2

def CalcSquareRootOfX(x):
    return math.sqrt(x)



def ArithemiticMenu():
    print("Start Simple Calculator Application")
    print("")
    print("")
    print("|==============================|")
    print("|        Simple Calculator 3   |")
    print("|==============================|")
    print("| 1. Addition                  |")
    print("| 2. Subtraction               |")
    print("| 3. Multiplication            |")
    print("| 4. Division                  |")
    print("| 5. Modulus                   |")
    print("| 6. Floor                     |")
    print("| 7. Exponent                  |")
    print("| 8. Square                    |")
    print("| 9. Square Root               |")
    print("| -1: Quit                     |")
    print("| =============================|")
    
    
def GetArithemiticMenu():
    choice = 1
    while choice > 0:
        ArithemiticMenu()
        choice = int(input("Enter Operation: "))
        if (choice == -1):
            break

        if ((choice > 9) or (choice < -1)):
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
        print(operand1, '+', operand2, '=', Addition(operand1, operand2))
    elif choice == 2:
        print(operand1, '-', operand2, '=', Subtraction(operand1,operand2))
    elif choice == 3:
        print(operand1, '*', operand2, '=', Multiplication(operand1,operand2))
    elif choice == 4:
        print(operand1, '/', operand2, '=', Division(operand1,operand2))
    elif choice == 5:
        print(operand1, '%', operand2, '=', Modulus(operand1,operand2))
    elif choice == 6:
        print(operand1, '//', operand2, '=', Floor(operand1,operand2))
    elif choice == 7:
        print(operand1, '**', operand2, '=', Exponent(operand1,operand2))
    elif choice == 8:
        print(operand1, '**', '2', '=', CalcSquareOfX(operand1))
    elif choice == 9:
        print('Square Root of', operand1, '=', CalcSquareRootOfX(operand1))
    else:
        pass # Break out


if __name__ == '__main__':
    GetArithemiticMenu()
    print("End Program: Have a good day")
    print("")

