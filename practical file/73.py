# Check if a string is palindrome
string = input("Enter a string: ")

# Reverse manually
reversed_string = ""
for i in range(len(string)-1, -1, -1):
    reversed_string += string[i]

if string == reversed_string:
    print("The string is a Palindrome.")
else:
    print("The string is NOT a Palindrome.")

print("this code is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
