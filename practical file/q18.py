start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

# Prime Numbers
print(f"\nPrime Numbers between {start} - {end}:")
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")

# Perfect Numbers
print(f"\n\nPerfect Numbers {start} - {end}: ")
for num in range(start, end + 1):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    if sum == num:
        print(num, end=" ")

# Armstrong Numbers
print(f"\n\nArmstrong Numbers {start} - {end}:")
for num in range(start, end + 1):
    temp = num
    digits = 0
    while temp > 0:
        temp  = temp // 10
        digits += 1

    temp = num
    root = 0
    sum = 0

    while temp > 0:
        root = temp % 10
        temp = temp // 10
        sum = root**digits + sum

    if sum == num:
        print(num, end=" ")
print("\n")

