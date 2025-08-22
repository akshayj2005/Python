for i in range(6):
    for j in range(i):
        print("*", end="")
    print()
print()
    
for i in range(1, 10):
        if i % 2 != 0:
            print(" " * (9-i) + "* " * i)
print()
        
for i in range(1, 10):
            print(" " * (9-i) + "*" * i)
print()

for i in range(1, 10):
            print(" " * (9-i) + "* " * i)
print()


for i in range(6):
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print()
print()

for i in range(5):
    for y in range(4-i):
        print(" ", end="")
    for j in range(65+i, 64, -1):
        print(chr(j), end="")
    print()
print()

for i in range(6):
    for j in range(1, 1 + i):
        print(j, end="")
    print()
print()

for i in range(5):
    for y in range(4-i):
        print(" ", end="")
    for j in range(1+i, 0, -1):
        print(j, end="")
    print()
print()

for i in range(1, 10):
    print( "*" * (9-i))
print()

for i in range(1, 10):
    print( " " * (i-1) +"*" * (9-i))
print()

for i in range(0, 5, 1):
            print(" " * (5-i) + " *" * i )
for i in range(5, 0, -1):
            print(" " * (5-i) + " *" * i )
print()

for i in range(5, 0, -1):
    print(" " * (5-i) + " *" * i )
for i in range(1, 5, 1):
    print(" " * (4-i) + " *" * (i+1) )
print()