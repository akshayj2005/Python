for num in range(10):
    if num % 2 == 0:
        continue
    print(num)  # This line will not execute for even numbers
print("Loop completed")  # This line will always execute


#continue using with a while loop
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
print("While loop completed")  # This line will always execute

