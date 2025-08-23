try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError as e:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError as e:
    print(e)
else:
    print(f"Result: {result}")
finally:
    print("Execution completed")  # This line will always execute
