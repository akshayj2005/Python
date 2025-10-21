def decorator_with_arg(msg):
    def decorator(func):
        def wrapper():
            print(msg)
            func()
        return wrapper
    return decorator

@decorator_with_arg("Custom message before function")
def say_hello():
    print("Hello!")

say_hello()
