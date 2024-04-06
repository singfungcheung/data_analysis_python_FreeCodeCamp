import numpy as np

a = np.array([1, 2, 3, 4])
# print(a >= 2)
# print(a[a >= 2])

"""
Exercises
"""

"""
1. Array Creation
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

# Create a numpy matrix of 4*4 integers, filled with fives.
# print(np.ones([4, 4]) * 5)

# Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with sevens.
# X = np.array([[2, 3], [6, 2]], dtype=np.int8)
# print(np.ones_like(X) * 7)

# Create a 3*3 identity numpy matrix with ones on the diagonal and zeros elsewhere.
# print(np.identity(3))
# print(np.eye(3))

# Create a numpy array, filled with 3 random integer values between 1 and 10.
# print(np.random.randint(10, size = 3))

# Create a 3*3*3 numpy matrix, filled with random float values
# print(np.random.rand(3, 3, 3))

# Given the X Python list convert it to an Y numpy array
# X = [1, 2, 3]
# print(X, type(X))

# Y = np.array(X)
# print(Y, type(Y))

# Given the X numpy array, make a copy and store it on Y.
# X = np.array([5, 2, 3], dtype=np.int8)
# print(X, id(X))

# Y = np.copy(X)
# print(Y, id(Y))

# Create a numpy array with numbers from 1 to 10.
# print(np.arange(1, 11))

# Create a numpy array with odd numbers from 1 to 10.
# print(np.arange(1, 11, 2))

# Create a numpy array with numbers from 1 to 10, in descending order.
# print(np.arange(1, 11)[::-1])

# Create a 3*3 numpy matrix, filled with values ranging from 0 to 8.
# print(np.arange(9).reshape(3,3))

# Show the memory size of the given Z numpy matrix
# Z = np.zeros((10, 10))
# print("%d bytes" % (Z.size * Z.itemsize))

"""
2. Array Indexation
"""