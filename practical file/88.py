#write a python code to demonstrate method overriding and method overloading.
# Method Overriding Example
class Animal:
    def sound(self):
        return "Some generic sound"
class Dog(Animal):
    def sound(self):
        return "Bark"
    
dog = Dog()
print(dog.sound())  # Output: Bark
# Method Overloading Example
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c
    def add(self, a, b):
        return a + b
math_ops = MathOperations()
print(math_ops.add(5, 10))        # Output: 15
print(math_ops.add(5, 10, 15))    # Output: 30

