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

# Given the X numpy array, show it's first element
# X = np.array(['A', 'B', 'C', 'D', 'E', 3])
# print(X[0])

# Given the X numpy array, show it's last element
# X = np.array(['A', 'B', 'C', 'D', 'E'])
# print(X[-1])

# Given the X numpy array, show it's first three elements
# X = np.array(['A', 'B', 'C', 'D', 'E'])
# print(X[:3])

# Given the X numpy array, show all middle elements
# X = np.array(['A', 'B', 'C', 'D', 'E'])
# print(X[1:-1])

# Given the X numpy array, show the elements in reverse position
# X = np.array(['A', 'B', 'C', 'D', 'E'])
# print(X[::-1])

# Given the X numpy array, show the elements in an odd position
# X = np.array(['A', 'B', 'C', 'D', 'E'])
# print(X[::2])

# Given the X numpy matrix, show the first row elements
# X = np.array([
#     [1,   2,  3,  4],
#     [5,   6,  7,  8],
#     [9,  10, 11, 12],
#     [13, 14, 15, 16]
# ])
# print(X[0, :])
#
# # Given the X numpy matrix, show the last row elements
# print(X[-1, :])
#
# # Show the first element of first row
# print(X[0, 0])
#
# # Show the last element of the last row
# print(X[-1, -1])
#
# # show the middle row elements
# print(X[1:-1, 1:-1])
#
# # Show the first 2 elements of the first 2 rows.
# print(X[0:2, 0:2])
#
# # Show the last 2 elements of the last 2 rows.
# print(X[-2:, -2:])

"""
3. Array Manipulation
"""
# Convert the given integer numpy to float
# X = [-5, -3, 0, 10, 40]
# print(np.array(X, dtype=float))

# Reverse the given numpy array (first element becomes last)
# print(X[::-1])

# sort the given numpy array
# X = [0, 10, -5, 40, -3]
# X.sort()
# print(X)

# Given the X numpy array, set the fifth element equal to 1
# X = np.zeros(10)
# X[4] = 1
# print(X)

# Given the X numpy array, change the 50 with a 40
# X = np.array([10, 20, 30, 50])
# X[3] = 40
# print(X)

# Given the X numpy matrix, change the last row with all 1
# X = np.array([
#     [1,   2,  3,  4],
#     [5,   6,  7,  8],
#     [9,  10, 11, 12],
#     [13, 14, 15, 16]
# ])
# X[3, :] = 1
# print(X)

# Given the X numpy matrix, change the last item on the last row with a 0.
# X[-1, -1] = 0
# print(X)

# Given the X numpy matrix, add 5 to every element.
# X[:] += 5
# print(X + 5)

"""
Boolean arrays (also called masks)
"""

# Given the X numpy array, make a mask showing negative elements
X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
# negative_mask = X < 0
# print(negative_mask)

# Get the negative elements
# print(X[negative_mask])

# Get numbers higher than 5.
# print(X[X > 5])

# Get numbers higher than mean.
# print(X[X > X.mean()])

# Get numbers equal to 2 or 10.
# print(X[(X == 2) | (X == 10)])

"""
Logic functions
"""

# Given the X numpy array, return True if none of its elements is zero
# print(X.all())

# Given the X numpy array, return True if any of its elements is zero
# print(X.any())

"""
Summary statistics
"""

# Given the numpy array, show the sum of its elements
# X = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4])
# print(X.sum())

# Show the mean value
# print(X.mean())

# show the sum of its columns
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
print(X.sum(axis=0))

# Given the X numpy matrix, show the mean value of its rows
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
print(X.mean(axis=1))

# Show the max value of elements
X = np.array([1, 2, 0, 4, 5, 6, 0, 0, 9, 10])
print(X.max())
print(np.max(X))