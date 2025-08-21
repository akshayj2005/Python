for num in range(10):
    if num % 2 == 0:
        continue
    print(num)  # This line will not execute for even numbers
print("Loop completed")  # This line will always execute