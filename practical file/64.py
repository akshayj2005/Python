#using simple function
def fibonacci_iterative(n):
    a, b = 0, 1
    series = []
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series

# Input
num = int(input("Enter a number: "))
print("Fibonacci Series (Iterative):", fibonacci_iterative(num))

#recursive function
def fibonacci_recursive(a, b, n, series):
    if a > n:
        return series
    series.append(a)
    return fibonacci_recursive(b, a + b, n, series)

# Input
num = int(input("Enter a number: "))
print("Fibonacci Series (Recursive):", fibonacci_recursive(0, 1, num, []))

print("This code is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
