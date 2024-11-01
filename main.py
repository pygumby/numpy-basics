"""NumPy: the absolute basics for beginners"""

import math
import numpy as np

########################################################################################
# NumPy: the absolute basics for beginners                                             #
########################################################################################
print("NumPy: the absolute basics for beginners")

########################################################################################
# Reading the example code                                                             #
########################################################################################
print("\nReading the example code\n")

a_0 = np.array([[1, 2, 3], [4, 5, 6]])
print(a_0.shape)  # (2, 3)

########################################################################################
# Array fundamentals                                                                   #
########################################################################################
print("\nArray fundamentals\n")

# One way to initialize an array is using a Python sequence, such as a list.
a_1 = np.array([1, 2, 3, 4, 5, 6])
print(a_1)  # [1 2 3 4 5 6]

# We can access an individual element of this array as we would access an element in the
# original list: using the integer index of the element within square brackets.
print(a_1[0])  # 1

# Like the original list, the array is mutable.
a_1[0] = 10
print(a_1)  # [10  2  3  4  5  6]

# Also like the original list, Python slice notation can be used for indexing.
print(a_1[:3])  # [10  2  3]

# One major difference is that slice indexing of a list copies the elements into a new
# list, but slicing an array returns a view: an object that refers to the data in the
# original array. The original array can be mutated using the view.
b_0 = a_1[3:]
print(b_0)  # [4 5 6]
b_0[0] = 40
print(a_1)  # [10  2  3 40  5  6]

# Two- and higher-dimensional arrays can be initialized from nested Python sequences.
a_2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a_2)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Another difference between an array and a list of lists is that an element of the
# array can be accessed by specifying the index along each axis within a single set of
# square brackets, separated by commas.
print(a_2[1, 3])  # 8

########################################################################################
# Array attributes                                                                     #
########################################################################################
print("\nArray attributes\n")

# The number of dimensions of an array is contained in the `ndim` attribute.
print(a_2.ndim)  # 2

# The `shape` of an array is a tuple of non-negative integers that specify the number of
# elements along each dimension.
print(a_2.shape)  # (3, 4)
print(a_2.ndim == len(a_2.shape))  # True

# The fixed, total number of elements in array is contained in the `size` attribute.
print(a_2.size)  # 12
print(a_2.size == math.prod(a_2.shape))  # True

# Arrays are typically "homogeneous", meaning that they contain elements of only one
# "data type". The data type is recorded in the `dtype` attribute.
print(a_2.dtype)  # int64

########################################################################################
# How to create a basic array                                                          #
########################################################################################
print("\nHow to create a basic array\n")

# Besides creating an array from a sequence of elements, you can easily create an array
# filled with `0`’s:
print(np.zeros(2))  # [0. 0.]

# Or an array filled with `1`’s:
print(np.ones(2))  # [1. 1.]

# Or even an empty array! The function `empty` creates an array whose initial content is
# random. The reason to use `empty` over `zeros` is speed.
print(np.empty(2))  # [3.14, 42.]

# You can create an array with a range of elements:
print(np.arange(4))  # [0 1 2 3]

# While the default data type is floating point (`np.float64`), you can explicitly
# specify which data type you want using the `dtype` keyword.
print(np.ones(2, dtype=np.int64))  # [1 1]

########################################################################################
# Adding, removing, and sorting elements                                               #
########################################################################################
print("\nAdding, removing, and sorting elements\n")

# You can quickly sort the numbers in ascending order with:
print(np.sort(np.array([2, 1, 5, 3, 7, 4, 6, 8])))

# You can concatenate arrays with `np.concatenate()`.
a_3 = np.array([1, 2, 3, 4])
b_1 = np.array([5, 6, 7, 8])
print(np.concatenate((a_3, b_0)))

x_0 = np.array([[1, 2], [3, 4]])
print(x_0.ndim)  # 2
print(x_0.shape)  # (2, 2)


y_0 = np.array([[5, 6]])
print(y_0.ndim)  # 2
print(y_0.shape)  # (1, 2)
print(np.concatenate((x_0, y_0), axis=0))
# [[1 2]
#  [3 4]
#  [5 6]]

y_1 = np.array([[5], [6]])
print(np.concatenate((x_0, y_1), axis=1))
# [[1 2 5]
#  [3 4 6]]
