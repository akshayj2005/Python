input_list = input("Enter integers separated by spaces: ").split()
int_list = [int(i) for i in input_list]
print("You entered the following integers:")
for num in int_list:
    print(num, end=' ')