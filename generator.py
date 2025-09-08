#create a simple generator
def simple_generator():
    count = 1
    while count <= 5:
        yield count
        count += 1

for value in simple_generator():
    print(value)



#use a geenerator with a loop
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)
    

#chain generators together
def generator1(max):
    count = 1
    while count <= 3:
        yield count
        count += 1

def generator2(numbers):
    for num in generator1():
        yield num ** 2

for squared in generator2(3):
    print(squared)

#fibonacci with generator expression
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b