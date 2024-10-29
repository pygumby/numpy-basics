"""NumPy: the absolute basics for beginners"""

import numpy as np

#
# Reading the example code
#

a_0 = np.array([[1, 2, 3], [4, 5, 6]])
print(a_0.shape) # (2, 3)

#
# Array fundamentals
#

# One way to initialize an array is using a Python sequence, such as a list.
a_1 = np.array([1, 2, 3, 4, 5, 6])
print(a_1) # [1 2 3 4 5 6]

# We can access an individual element of this array as we would access an element in the
# original list: using the integer index of the element within square brackets.
print(a_1[0]) # 1

# Like the original list, the array is mutable.
a_1[0] = 10
print(a_1) # [10  2  3  4  5  6]

# Also like the original list, Python slice notation can be used for indexing.
print(a_1[:3]) # [10  2  3]

# One major difference is that slice indexing of a list copies the elements into a new
# list, but slicing an array returns a view: an object that refers to the data in the
# original array. The original array can be mutated using the view.
b_0 = a_1[3:]
print(b_0) # [4 5 6]
b_0[0] = 40
print(a_1) # [10  2  3 40  5  6]

# Two- and higher-dimensional arrays can be initialized from nested Python sequences.
a_2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a_2)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Another difference between an array and a list of lists is that an element of the
# array can be accessed by specifying the index along each axis within a single set of
# square brackets, separated by commas.
print(a_2[1, 3]) # 8
