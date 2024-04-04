import numpy as np

a = np.array([1, 2, 3, 4])
# print(a >= 2)
# print(a[a >= 2])

"""
Exercises
"""

# Version of Python
# print("Python version: " + np.__version__)

# Create a numpy array of size 10, filled with zeros.
# print(np.zeros(10))

# Create a numpy array with values randing from 10 to 49
# print(np.arange(10, 50))

# Create a numpy matrix of 2x2, filled with ones.
# print(np.ones([2, 2], dtype=np.int8))

# Create a numpy matrix of 3*2 float numbers, filled with ones.
# print(np.ones([3, 2], dtype=np.float16))

# Given the X numpy array, create a new numpy array with the same shape and type as X, filled with ones.
# X = np.arange(4, dtype=np.int8)
# print(np.ones_like(X))

# Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with zeros.
# X = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int8)
# print(np.zeros_like(X))
