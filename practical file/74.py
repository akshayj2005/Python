# Calculate length of a string without using len()
string = input("Enter a string: ")

count = 0
for char in string:
    count += 1

print("Length of string:", count)

