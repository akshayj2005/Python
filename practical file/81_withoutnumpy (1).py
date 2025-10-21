# Define two 3x3 matrices
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# Addition
addition = [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]

# Subtraction
subtraction = [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]

# Multiplication
multiplication = [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

# Transpose of A
transpose_A = [[A[j][i] for j in range(3)] for i in range(3)]

# Transpose of B
transpose_B = [[B[j][i] for j in range(3)] for i in range(3)]

# Print results
print("Matrix Addition:")
for row in addition:
    print(row)

print("\nMatrix Subtraction:")
for row in subtraction:
    print(row)

print("\nMatrix Multiplication:")
for row in multiplication:
    print(row)

print("\nTranspose of Matrix A:")
for row in transpose_A:
    print(row)

print("\nTranspose of Matrix B:")
for row in transpose_B:
    print(row)
