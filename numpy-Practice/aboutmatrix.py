'''
====================
Matrix Basics for ML
====================

Definitions:
-----------
Scalar: A single number (e.g., 5)
Vector: A 1D array of numbers (e.g., [1, 2, 3])
Matrix: A 2D array of numbers (e.g., [[1,2,3],[4,5,6],[7,8,9]])
Tensor: An n-dimensional array (generalization of matrix)

Matrix Example:
---------------
    [ 1  2  3 ]
    [ 4  5  6 ]
    [ 7  8  9 ]

Rows: Horizontal lines (e.g., [1,2,3])
Columns: Vertical lines (e.g., [1,4,7])
Size: rows × columns (here, 3 × 3)

Matrix in ML:
-------------
- Data is often stored as matrices (rows = samples, columns = features)
- Images are matrices of pixel values
- Matrix operations are used in linear regression, neural networks, PCA, etc.

Common Matrix Operations:
------------------------
- Addition: element-wise
- Multiplication: dot product (matrix product)
- Transpose: swap rows and columns
- Inverse: only for square matrices

NumPy Matrix Examples:
---------------------
import numpy as np

# Create a matrix
A = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Shape
print("Shape:", A.shape)  # (3, 3)

# Transpose
print("Transpose:\n", A.T)

# Matrix multiplication
B = np.array([[1,0,0],[0,1,0],[0,0,1]])
print("A @ B:\n", A @ B)

# Element-wise addition
print("A + B:\n", A + B)

# Access row/column
print("First row:", A[0])
print("First column:", A[:,0])

# Inverse (only for invertible matrices)
C = np.array([[1,2],[3,4]])
print("Inverse of C:\n", np.linalg.inv(C))

Further Reading:
----------------
- https://numpy.org/doc/stable/user/quickstart.html
- https://en.wikipedia.org/wiki/Matrix_(mathematics)
- https://machinelearningmastery.com/linear-algebra-for-machine-learning/
'''