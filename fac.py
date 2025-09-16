num = int(input("Enter a number to find its factorial: "))
# #factorial of a given number using recursion
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# result = factorial(num)
# print(f"The factorial of {num} is {result}")
#functional approach to find factorial
def fac(num):
    b=1
    for i in range(1,num+1):
        b=b * (i)
    return b
print(f"The factorial of {num} is {fac(num)}")

# print(f"Factorial of {i} is {factorial(i)}")