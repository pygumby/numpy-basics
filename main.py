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
# filled with `0`'s:
print(np.zeros(2))  # [0. 0.]

# Or an array filled with `1`'s:
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

########################################################################################
# How do you know the shape and size of an array?                                      #
########################################################################################
print("\nHow do you know the shape and size of an array?\n")

a_4 = np.array(
    [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
    ]
)

# `ndarray.ndim` will tell you the number of axes, or dimensions, of the array`
print(a_4.ndim)

# `ndarray.size` will tell you the total number of elements of the array. This is the
# product of the elements of the array's shape.
print(a_4.size)

# `ndarray.shape` will display a tuple of integers that indicate the number of elements
# stored along each dimension of the array. If, for example, you have a 2-D array with 2
# rows and 3 columns, the shape of your array is (2, 3).
print(a_4.shape)

########################################################################################
# How to convert a 1D array into a 2D array                                            #
########################################################################################
print("\nHow to convert a 1D array into a 2D array\n")

# Using `np.newaxis` will increase the dimensions of your array by one dimension when
# used once. This means that a 1D array will become a 2D array, a 2D array will become a
# 3D array, and so on.
a_5 = np.array([1, 2, 3, 4, 5, 6])
print(a_5.shape)  # (6,)

a_6 = a_5[np.newaxis, :]
print(a_6.shape)  # (1, 6)
print(a_6)  # [[1 2 3 4 5 6]]

# You can explicitly convert a 1D array to either a row vector or a column vector using
# `np.newaxis`.
row_vector = a_5[np.newaxis, :]
print(row_vector.shape)  # (1, 6)
print(row_vector)  # [[1 2 3 4 5 6]]

col_vector = a_5[:, np.newaxis]
print(col_vector.shape)  # (6, 1)
print(col_vector)
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]

# You can also expand an array by inserting a new axis at a specified position with
# `np.expand_dims`. You can use `np.expand_dims`` to add an axis at index position 1
# with:
b_2 = np.expand_dims(a_5, axis=1)
print(b_2.shape)  # (6, 1)
print(b_2)
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]

c_0 = np.expand_dims(a_5, axis=0)
print(c_0.shape)  # (1, 6)
print(c_0)  # [[1 2 3 4 5 6]]

########################################################################################
# Indexing and slicing                                                                 #
########################################################################################
print("\nIndexing and slicing\n")

# You can index and slice NumPy arrays in the same ways you can slice Python lists.
data = np.array([1, 2, 3])

print(data[1])  # 2
print(data[0:2])  # [1 2]
print(data[1:])  # [2 3]
print(data[-2:])  # [2 3]

# If you want to select values from your array that fulfill certain conditions, it's
# straightforward with NumPy.
a_7 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# You can easily print all of the values in the array that are less than 5.
print(a_7[a_7 < 5])  # [1 2 3 4]

# You can also select numbers that are equal to or greater than 5, and use that
# condition to index an array.
five_up = a_7 >= 5
print(five_up)
# [[False False False False]
#  [ True  True  True  True]
#  [ True  True  True  True]]
print(a_7[five_up])
# [ 5  6  7  8  9 10 11 12]

# You can select elements that are divisible by 2:
divisible_by_2 = a_7[a_7 % 2 == 0]
print(divisible_by_2)  # [ 2  4  6  8 10 12]

# Or you can select elements that satisfy two conditions using the `&` and `|`
# operators:
c_1 = a_7[(a_7 > 2) & (a_7 < 11)]
print(c_1)  # [ 3  4  5  6  7  8  9 10]

# You can also use `np.nonzero()` to select elements or indices from an array. In this
# example, a tuple of arrays is returned: one for each dimension. The first array
# represents the row indices where these values are found, and the second array
# represents the column indices where the values are found.
b_3 = np.nonzero(a_7 < 5)
print(b_3)  # (array([0, 0, 0, 0]), array([0, 1, 2, 3]))

# If you want to generate a list of coordinates where the elements exist, you can zip
# the arrays, iterate over the list of coordinates, and print them.
list_of_coordinates = list(zip(b_3[0], b_3[1]))
for coord in list_of_coordinates:
    print(coord)
# (np.int64(0), np.int64(0))
# (np.int64(0), np.int64(1))
# (np.int64(0), np.int64(2))
# (np.int64(0), np.int64(3))

# You can also use `np.nonzero()` to print the elements in an array that are less than 5
# with:
print(a_7[b_3])  # [1 2 3 4]

# If the element you're looking for doesn't exist in the array, then the returned array
# of indices will be empty.
not_there = np.nonzero(a_7 == 42)
print(not_there)
# (array([], dtype=int64), array([], dtype=int64))

########################################################################################
# How to create an array from existing data                                            #
########################################################################################
print("\nHow to create an array from existing data\n")

a_8 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# You can create a new array from a section of your array any time by specifying where
# you want to slice your array.
arr_0 = a_8[3:8]
print(arr_0)  # [4 5 6 7 8]

# You can also stack two existing arrays, both vertically and horizontally.
a_9 = np.array([[1, 1], [2, 2]])
a_10 = np.array([[3, 3], [4, 4]])

print(np.vstack((a_9, a_10)))
# [[1 1]
#  [2 2]
#  [3 3]
#  [4 4]]

print(np.hstack((a_9, a_10)))
# [[1 1 3 3]
#  [2 2 4 4]]

# You can use the `view` method to create a new array object that looks at the same data
# as the original array (a shallow copy). Views are an important NumPy concept! NumPy
# functions, as well as operations like indexing and slicing, will return views whenever
# possible. This saves memory and is faster (no copy of the data has to be made).
# However it's important to be aware of this - modifying data in a view also modifies
# the original array!
a_11 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

b_4 = a_11[0, :]
print(b_4)  # [1 2 3 4]

b_4[0] = 99
print(b_4)  # [99  2  3  4]
print(a_11)
# [[99  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Using the copy method will make a complete copy of the array and its data (a deep
# copy).
b_5 = a_11.copy()

########################################################################################
# Basic array operations                                                               #
########################################################################################
print("\nBasic array operations\n")

data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(data + ones)  # [2 3]
print(data - ones)  # [0 1]
print(data * data)  # [1 4]
print(data / data)  # [1. 1.]

# If you want to find the sum of the elements in an array, you'd use `sum()`.
a_12 = np.array([1, 2, 3, 4])
print(a_12.sum())

# To add the rows or the columns in a 2D array, you would specify the axis.
b_6 = np.array([[1, 1], [2, 2]])
print(b_6.sum(axis=0))  # [3 3]
print(b_6.sum(axis=1))  # [2 4]
