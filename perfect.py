print("enter your number")
x = int(input('Number:->   '))
count = 0
for i in range(1,x):
    if x % i == 0:
        count +=i

if count == x:
    print("its a perfect number ", x)
else:
    print("Not a perfect number ", x)