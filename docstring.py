# #doc string demonstrating how to use docstrings in Python
# def add(a, b): 
#     """Returns the sum of a and b.
    
#     Parameters:
#     a (int, float): The first number.
#     b (int, float): The second number.
    
#     Returns:
#     int, float: The sum of a and b.
#     """
#     return a + b

# print(add.__doc__)  # Output: 8

#define decorator function
def decorator_function(original_function):
    def wrapper_function():
        print("submit code before executing the function")
        original_function()
        print("submit code after executing the function")
    return wrapper_function
@decorator_function

def display():
    print("Display function executed")
display()

#decorator with arguments
def repeat(num_times):
    def decorator_repeat(original_function):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                original_function(*args, **kwargs)
        return wrapper
    return decorator_repeat
@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

#demonstrate decorator usning function tools.wraps
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper
@my_decorator
def say_hello(name):
    """Greets a person by name."""
    print(f"Hello, {name}!")
say_hello("Bob")

#decorator logging example
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper
@log_function_call
def multiply(x, y):
    return x * y
multiply(3, 4)

# def longest_common_substring(strings):
#     shortest = min(strings, key=len)
#     for length in range(len(shortest), 0, -1):
#         for start in range(len(shortest) - length + 1):
#             part = shortest[start:start+length]
#             if all(part in s for s in strings):
#                 return part
#     return ""
    

# string1 = "pythHello, World!","pythiusdvjk","Python is great for data science."
# result = longest_common_substring(string1)
# print("Longest common substring:", result)



s = input("Enter a Roman numeral: ").upper()
fd = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
b = 0

for i in range(len(s)):
    if i + 1 < len(s) and fd[s[i]] < fd[s[i + 1]]:
        b -= fd[s[i]]
    else:
        b += fd[s[i]]

print("Integer value:", b)

