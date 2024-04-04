import numpy as np

a = np.array([1, 2, 3, 4])
# print(a >= 2)
# print(a[a >= 2])

"""
Exercises
"""

# Version of Python
print("Python version: " + np.__version__)

# Create a numpy array of size 10, filled with zeros.
print(np.zeros(10))

# Create a numpy array with values randing from 10 to 49
print(np.arange(10, 50))

# Create a numpy matrix of 2x2, filled with ones.
print(np.ones([2, 2], dtype=np.int8))

# Create a numpy matrix of 3*2 float numbers, filled with ones.
print(np.ones([3, 2], dtype=np.float16))

