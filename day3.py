import numpy as np

# Creating a 1D array from a Python list
arr_1d = np.array([1, 2, 3, 4, 5])

# Creating a 2D array (Matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Creating an array filled with zeros
zeros = np.zeros((2, 3))  # Argument is a tuple: (rows, columns)

# Creating an array filled with ones
ones = np.ones((3, 3))

# Creating an array with a range of values (start, stop, step)
range_arr = np.arange(0, 10, 2)  # Output: [0, 2, 4, 6, 8]

# Creating evenly spaced numbers over a specified interval
linspace_arr = np.linspace(0, 1, 5)  # Output: [0. , 0.25, 0.5 , 0.75, 1. ]
