# Reverse a string without using predefined functions
string = input("Enter a string: ")

reversed_string = ""
for i in range(len(string)-1, -1, -1):
    reversed_string += string[i]

print("Reversed string:", reversed_string)
print("This code is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
