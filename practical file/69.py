# Function returning multiple values
def arithmetic_operations(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val, diff_val

sum_result, diff_result = arithmetic_operations(10, 5)
print("Sum:", sum_result)
print("Difference:", diff_result)

