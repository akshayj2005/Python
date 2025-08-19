count = 0
print("Perfect Numbers from 1 to 2025:")

for num in range(1, 2026):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    if sum == num:
        print(num, end=" ")
        count = count + 1

print("\n\nTotal Perfect Numbers:", count)
