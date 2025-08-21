#break statement in while loop
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        break
    print(num)
print("While loop completed")  # This line will not execute if the loop is broken

