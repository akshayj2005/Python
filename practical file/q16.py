num = int(input("Enter a number: "))
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
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
