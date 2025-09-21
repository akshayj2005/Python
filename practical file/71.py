# Program to print all Armstrong numbers in a given range

# Function to check Armstrong number
def is_armstrong(num):
    order = len(str(num))   # number of digits
    sum_of_powers = sum(int(digit) ** order for digit in str(num))
    return num == sum_of_powers

# Taking range input from user
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

print(f"Armstrong numbers between {start} and {end} are:")
for i in range(start, end + 1):
    if is_armstrong(i):
        print(i)

