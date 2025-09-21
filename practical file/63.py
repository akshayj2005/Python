def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Taking input from the user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")
    
print("This code is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
