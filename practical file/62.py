def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive call

# Taking input from the user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")
print("This code is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
