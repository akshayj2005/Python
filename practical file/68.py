# Function with default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # Uses default parameter
greet("Alice")    # Overrides default parameter

