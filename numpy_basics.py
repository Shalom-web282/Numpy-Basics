"""
NumPy Basics Day 2: Practice Questions
Author: SHALOM CHUKWUKADIBIA CHIMDIKE
Description:
This script covers foundational NumPy concepts including:
- Array creation
- Shape and dimensions
- Data types
- Reshaping
- Indexing & slicing
- Boolean masking

"""

import numpy as np


# QUESTION 1: Array Creation & Attributes

A = np.arange(5, 26, 5)

print("Array A:", A)
print("Shape:", A.shape)
print("Dimensions:", A.ndim)
print("Data type:", A.dtype)
print("Total elements:", A.size)

print("Linspace example:", np.linspace(0, 1, 5))


# QUESTION 2: Reshaping & Data Types


B = np.full((4, 3), 1)
B = B.astype(np.float32)
B = B.reshape((3, 4))

print("\nReshaped B:\n", B)
print("Data type of B:", B.dtype)


# QUESTION 3: Indexing & Slicing

M = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("\nSecond row:", M[1])
print("First column:", M[:, 0])
print("Element 110:", M[2, 2])
print("Last column:", M[:, 3])
print("First two rows:\n", M[0:2])
print("Bottom-right 2x3 block:\n", M[1:3, 1:4])


# QUESTION 4: Advanced Slicing

print("\nMiddle 2x2 block:\n", M[1:3, 1:3])
print("Bottom row:", M[2])
print("Everything except first column:\n", M[:, 1:4])
print("Top-right 2x2 block:\n", M[0:2, 1:3])


# QUESTION 5: Boolean Masking

print("\nValues greater than 60:", M[M > 60])
print("Values between 30 and 100:", M[(M > 30) & (M < 100)])
print("Count greater than 75:", np.sum(M > 75))

M[M < 50] = 0
print("Matrix after replacing values < 50 with 0:\n", M)
