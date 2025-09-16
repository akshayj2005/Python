#demonstrate function definition and calling
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

def add(a, b):
    return a + b

#default parameters
def greet (name="Guest"):
    return f"Hello, {name}!"
print(greet())
print(greet("Bob"))

#multiple return values
def arithmetic_operations(x, y):
    return x + y, x - y, x * y, x / y

#function that returns list/dictionary
def get_square(numbers):
    return [x**2 for x in numbers]
nums = [1, 2, 3, 4]
squares_list = get_square(nums)
print(squares_list)