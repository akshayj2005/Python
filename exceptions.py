try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError as e:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
print("Execution completed")  # This line will always execute
print("End of program")  # This line will always execute
print("\n\n\n\n\n")

#try except and else
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError as e:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Result: {result}")
finally:
    print("Execution completed")  # This line will always execute
print("\n\n\n\n\n")


#try except with finally
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error: The file was not found.")
except IOError as e:
    print("Error: An I/O error occurred.")
finally:
    if 'file' in locals():
        file.close()
    print("File operation completed")
    
    