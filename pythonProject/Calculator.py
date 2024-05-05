import math
import sys

# A function for addition


def addition():
    num1 = int(input("Provide your first number: "))
    num2 = int(input("Provide your second number: "))
    print(num1 + num2)

# A function for subtraction


def subtraction():
    num1 = int(input("Provide your first number: "))
    num2 = int(input("Provide your second number: "))

    print(num1 - num2)

# A function for multiplication


def multiplication():
    num1 = int(input("Provide your first number: "))
    num2 = int(input("Provide your second number: "))
    print(num1 * num2)

# A function for division


def division():
    num1 = int(input("Provide your first number: "))
    num2 = int(input("Provide your second number: "))
    if num2 == 0:
        print("Huh?")
        sys.exit(0)
    else:
        print(num1 / num2)

# A function for floor


def floor():
    num1 = int(input("Provide your first number: "))
    num2 = int(input("Provide your second number: "))
    if num2 == 0:
        print("That's Mathematically wrong!")
        sys.exit(0)
    else:
        print(num1 // num2)

# A function for exponent


def exponent():
    num1 = int(input("Provide your first number: "))
    num2 = int(input("Provide your second number: "))
    print(num1 ** num2)

# A function for square root


def square_root():
    num1 = int(input("Provide the number: "))
    num1 = math.sqrt(num1)
    print(num1)


if __name__ == "__main__":
    print("Pick a mode from 1 - 7"
          "\n1 = addition"
          "\n2 = subtraction"
          "\n3 = multiplication"
          "\n4 = division"
          "\n5 = floor"
          "\n6 = exponent"
          "\n7 = square root")
    choice = int(input("Enter your choice: "))
    if choice > 7 or choice < 1:
        print("Error!")
    if choice == 1:
        print(addition())
    elif choice == 2:
        print(subtraction())
    elif choice == 3:
        print(multiplication())
    elif choice == 4:
        print(division())
    elif choice == 5:
        print(floor())
    elif choice == 6:
        print(exponent())
    if choice == 7:
        print(square_root())
