#menu based calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def power(x, y):
    return x ** y
def modulus(x, y):
    return x % y
def floor_divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y
def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of negative number."
    return x ** 0.5
def cube_root(x):
    return x ** (1/3)
def factorial(x):
    if x < 0:
        return "Error! Factorial of negative number doesn't exist."
    elif x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result
def percentage(x, y):
    return (x / y) * 100
def logarithm(x, base):
    import math
    if x <= 0 or base <= 1:
        return "Error! Logarithm undefined for these values."
    return math.log(x, base)

def display_menu():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Division")
    print("8. Square Root")
    print("9. Cube Root")
    print("10. Factorial")
    print("11. Percentage")
    print("12. Logarithm")
    print("13. Exit")
    print("14. Help")
    input("Enter choice(1-14): ")
    choice = int(input())
    return choice
def main():
    while True:
        choice = display_menu()
        if choice == 13:
            print("Exiting the calculator. Goodbye!")
            break
        elif choice == 14:
            print("This is a simple calculator that can perform various operations.")
            print("Select the operation by entering the corresponding number.")
            continue
        if choice in [1, 2, 3, 4, 5, 6, 7, 11, 12]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        elif choice in [8, 9, 10]:
            num1 = float(input("Enter the number: "))
        else:
            print("Invalid input. Please select a valid operation.")
            continue

        if choice == 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 3:
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 4:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == 5:
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == 6:
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
        elif choice == 7:
            print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
        elif choice == 8:
            print(f"Square root of {num1} = {square_root(num1)}")
        elif choice == 9:
            print(f"Cube root of {num1} = {cube_root(num1)}")
        elif choice == 10:
            print(f"Factorial of {int(num1)} = {factorial(int(num1))}")
        elif choice == 11:
            print(f"{num1} is {percentage(num1, num2)}% of {num2}")
        elif choice == 12:
            base = float(input("Enter the base for logarithm: "))
            print(f"log base {base} of {num1} = {logarithm(num1, base)}")
        else:
            print("Invalid input. Please select a valid operation.")