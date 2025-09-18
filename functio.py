# num = int(input("Enter a number to find its factorial: "))
# #factorial of a given number using recursion
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# result = factorial(num)
# print(f"The factorial of {num} is {result}")
# #functional approach to find factorial
# def fac(num):
#     b=1
#     for i in range(1,num+1):
#         b=b * (i)
#     return b
# print(f"The factorial of {num} is {fac(num)}")

# print(f"Factorial of {i} is {factorial(i)}")

# n = int(input("Enter the number of terms for Fibonacci series: "))
# #print fibonacci series
# def fibonacci(n):
#     fib = [0, 1]
#     for i in range(2, n):
#         next_fib = fib[-1] + fib[-2]
#         fib.append(next_fib)
#     return fib[:n]
# print(f"Fibonacci series up to {n} terms: {fibonacci(n)}")

# #fibonacci using recursion
# def fib_rec(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib = fib_rec(n - 1)
#         fib.append(fib[-1] + fib[-2])
#         return fib
# print(f"Fibonacci series up to {n} terms using recursion: {fib_rec(n)}")

# #demonstrate global variable
# x = 10  # global variable
# def modify_global():
#     global x
#     x += 5
#     return x
# print(f"Modified global variable: {modify_global()}")
# print(f"Global variable x: {x}")

# #armstrong number
# num = int(input("Enter a number to check if it's an Armstrong number: "))
# def is_armstrong(n):
#     num_str = str(n)
#     num_digits = len(num_str)
#     sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
#     return sum_of_powers == n
# if is_armstrong(num):
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")

# #armstrong number in a range with recursion
# def armstrong_in_range(start, end):
#     armstrong_numbers = []
#     for num in range(start, end + 1):
#         if is_armstrong(num):
#             armstrong_numbers.append(num)
#     return armstrong_numbers
#armstrong number in a range without recursion
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
def armstrong_in_range_no_rec(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        sum_of_powers = sum(int(digit) ** len(str(num)) for digit in str(num))
        if sum_of_powers == num:
            armstrong_numbers.append(num)
    return armstrong_numbers
# print(f"Armstrong numbers between {start_range} and {end_range}: {armstrong_in_range(start_range, end_range)}")
print(f"Armstrong numbers between {start_range} and {end_range} without recursion: {armstrong_in_range_no_rec(start_range, end_range)}")



