x = 10  # global variable

def outer():
    def inner():
        global x
        x = 20  # modify global variable
        print("Inner x:", x)
    inner()
    print("Outer x:", x)

outer()
print("Global x:", x)
