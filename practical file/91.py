#deletion  of objct explicitely
class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created.")

obj2 = MyClass(10)
obj1 = obj2
del obj1  # Explicitly deleting obj1
del obj2  # Explicitly deleting obj2
