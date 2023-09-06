# Simple Calculator Application
import math


def ConvDegCentDegFahr(c):
    return (1.8*c) + 32

def ConvDegFahrDegCent(f):
    return (f - 32) / 1.8

def ConversionMenu():
    print("Start Simple Calculator Application")
    print("")
    print("|==============================|")
    print("|       Conversions 3          |")
    print("|==============================|")
    print("| 1. Convert Cent To Fahr      |")
    print("| 2. Convert Fahr To Cent      |")
    print("| -1: Quit                     |")
    print("| =============================|")
    
    
def GetConversionMenuChoice():
    choice = 1
    while choice > 0:
        ConversionMenu()
        choice = int(input("Enter Operation: "))
        if (choice == -1):
            break
    
        if ((choice > 2) or (choice < -1)):
            print("ERROR: Invalid Choice of Operation")
            print("Please Try again")
            choice = 1
            continue
    
        operand1 = int(input("Enter First Operand: "))
        PrintOutput(choice, operand1)

def PrintOutput(choice, operand1, operand2=0):  #Operand2 has a default value of 0
    if choice == 1:
        print(operand1, 'converted to Degree Fahrenheit', '=', ConvDegCentDegFahr(operand1))

    elif choice == 2:
        print(operand1, 'converted to Degree Centigrade', '=', ConvDegFahrDegCent(operand1))
    else:
        pass # Break out of the while loop

if __name__ == '__main__':
    GetConversionMenuChoice()
    print("End Program: Have a good day")
    print("")

