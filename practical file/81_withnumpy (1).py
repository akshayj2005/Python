import numpy as np

# Define two 3x3 matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Addition
print("Matrix Addition:\n", A + B)

# Subtraction
print("\nMatrix Subtraction:\n", A - B)

# Multiplication (Matrix product)
print("\nMatrix Multiplication:\n", np.dot(A, B))

# Transpose
print("\nTranspose of Matrix A:\n", A.T)
print("\nTranspose of Matrix B:\n", B.T)
