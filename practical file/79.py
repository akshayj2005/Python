from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    """This function says hello."""
    print("Hello!")

say_hello()
print(say_hello.__name__)  # Outputs: say_hello
print(say_hello.__doc__)   # Outputs: This function says hello.
