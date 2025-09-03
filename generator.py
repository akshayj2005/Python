#create a simple generator
def simple_generator():
    count = 1
    while count <= 5:
        yield count
        count += 1

for value in simple_generator():
    print(value)