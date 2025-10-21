# Program to perform addition, subtraction, multiplication, and transpose of 3x3 matrices

# Define two 3x3 matrices
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# Function to print matrix
def print_matrix(matrix, name="Matrix"):
    print(f"\n{name}:")
    for row in matrix:
        print(row)

# Matrix Addition
def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]

# Matrix Subtraction
def sub_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]

# Matrix Multiplication
def mul_matrix(A, B):
    result = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Matrix Transpose
def transpose_matrix(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


# Printing results
print_matrix(A, "Matrix A")
print_matrix(B, "Matrix B")

print_matrix(add_matrix(A, B), "Addition (A + B)")
print_matrix(sub_matrix(A, B), "Subtraction (A - B)")
print_matrix(mul_matrix(A, B), "Multiplication (A * B)")
print_matrix(transpose_matrix(A), "Transpose of A")
print_matrix(transpose_matrix(B), "Transpose of B")

print("This code is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063.")
