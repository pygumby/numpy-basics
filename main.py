"""NumPy: the absolute basics for beginners"""

import math
import numpy as np
import pandas as pd

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
data_0 = np.array([1, 2, 3])

print(data_0[1])  # 2
print(data_0[0:2])  # [1 2]
print(data_0[1:])  # [2 3]
print(data_0[-2:])  # [2 3]

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

data_1 = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(data_1 + ones)  # [2 3]
print(data_1 - ones)  # [0 1]
print(data_1 * data_1)  # [1 4]
print(data_1 / data_1)  # [1. 1.]

# If you want to find the sum of the elements in an array, you'd use `sum()`.
a_12 = np.array([1, 2, 3, 4])
print(a_12.sum())

# To add the rows or the columns in a 2D array, you would specify the axis.
b_6 = np.array([[1, 1], [2, 2]])
print(b_6.sum(axis=0))  # [3 3]
print(b_6.sum(axis=1))  # [2 4]

########################################################################################
# Broadcasting                                                                         #
########################################################################################
print("\nBroadcasting\n")

# There are times when you might want to carry out an operation between an array and a
# single number (also called an operation between a vector and a scalar) or between
# arrays of two different sizes.

# NumPy understands that the following multiplication should happen with each cell. That
# concept is called broadcasting. Broadcasting is a mechanism that allows NumPy to
# perform operations on arrays of different shapes. The dimensions of your array must be
# compatible, for example, when the dimensions of both arrays are equal or when one of
# them is 1.
data_2 = np.array([1.0, 2.0])
print(data_2 * 1.6)  # [1.6 3.2]

########################################################################################
# More useful array operations                                                         #
########################################################################################
print("\nMore useful array operations\n")

# NumPy also performs aggregation functions. In addition to `min`, `max`, and `sum`, you
# can easily run `mean` to get the average, `prod` to get the result of multiplying the
# elements together, `std` to get the standard deviation, and more.
data_3 = np.array([1.0, 2.0])
print(data_3.max())  # 2.0
print(data_3.min())  # 1.0
print(data_3.sum())  # 3.0

# Let's start with this array, called `a`:
a_13 = np.array(
    [
        [0.45053314, 0.17296777, 0.34376245, 0.5510652],
        [0.54627315, 0.05093587, 0.40067661, 0.55645993],
        [0.12697628, 0.82485143, 0.26590556, 0.56917101],
    ]
)
print(a_13.sum())  # 4.8595784
print(a_13.min())  # 0.05093587

# You can specify on which axis you want the aggregation function to be computed. For
# example, you can find the minimum value within each column by specifying `axis=0`.
print(a_13.min(axis=0))  # [0.12697628 0.05093587 0.26590556 0.5510652 ]

########################################################################################
# Creating matrices                                                                    #
########################################################################################
print("\nCreating matrices\n")

# You can pass Python lists of lists to create a 2-D array (or "matrix") to represent
# them in NumPy.

data_4 = np.array([[1, 2], [3, 4], [5, 6]])
print(data_4)
# [[1 2]
#  [3 4]
#  [5 6]]

# Indexing and slicing operations are useful when you're manipulating matrices:
print(data_4[0, 1])  # 2
print(data_4[1:3])
# [[3 4]
#  [5 6]]
print(data_4[0:2, 0])  # [1 3]

# You can aggregate matrices the same way you aggregated vectors:
print(data_4.max())  # 6
print(data_4.min())  # 1
print(data_4.sum())  # 21

# You can aggregate all the values in a matrix and you can aggregate them across columns
# or rows using the `axis` parameter.
data_5 = np.array([[1, 2], [5, 3], [4, 6]])
print(data_5)
# [[1 2]
#  [5 3]
#  [4 6]]
print(data_5.max(axis=0))  # [5 6]
print(data_5.max(axis=1))  # [2 5 6]

# You can do these arithmetic operations on matrices of different sizes, but only if one
# matrix has only one column or one row. In this case, NumPy will use its broadcast
# rules for the operation.
data_6 = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([1, 1])
print(data_6 + ones_row)
# [[2 3]
#  [4 5]
#  [6 7]]

# Be aware that when NumPy prints N-dimensional arrays, the last axis is looped over the
# fastest while the first axis is the slowest.
print(np.ones((4, 3, 2)))
# [[[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]]

# There are often instances where we want NumPy to initialize the values of an array.
# NumPy offers functions like `ones()` and `zeros()`, and the `random.Generator` class
# for random number generation for that.
print(np.ones(3))  # [1. 1. 1.]
print(np.zeros(3))  # [0. 0. 0.]
rng = np.random.default_rng()
print(rng.random(3))  # [0.04684997 0.89084346 0.15499562]

# You can also use `ones()`, `zeros()`, and `random()` to create a 2D array if you give
# them a tuple describing the dimensions of the matrix:
print(np.ones((3, 2)))
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]
print(np.zeros((3, 2)))
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]
print(rng.random((3, 2)))
# [[0.70594248 0.02637369]
#  [0.85647803 0.11083294]
#  [0.07493274 0.36550293]]

########################################################################################
# How to get unique items and counts                                                   #
########################################################################################
print("\nHow to get unique items and counts\n")

a_14 = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])

# You can find the unique elements in an array easily with `np.unique`.
unique_values_0 = np.unique(a_14)
print(unique_values_0)  # [11 12 13 14 15 16 17 18 19 20]

# To get the indices of unique values in a NumPy array (an array of first index
# positions of unique values in the array), just pass the `return_index` argument in
# `np.unique()` as well as your array.
unique_values_1, indices_list = np.unique(a_14, return_index=True)
print(indices_list)  # [ 0  2  3  4  5  6  7 12 13 14]

# You can pass the `return_counts` argument in `np.unique()` along with your array to
# get the frequency count of unique values in a NumPy array.
unique_values_2, occurrence_count = np.unique(a_14, return_counts=True)
print(occurrence_count)  # [3 2 2 2 1 1 1 1 1 1]

# This also works with 2D arrays! If the axis argument isn't passed, your 2D array will
# be flattened.
a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
print(np.unique(a_2d))  # [ 1  2  3  4  5  6  7  8  9 10 11 12]

# If you want to get the unique rows or columns, make sure to pass the axis argument. To
# find the unique rows, specify `axis=0` and for columns, specify `axis=1`.
unique_rows = np.unique(a_2d, axis=0)
print(unique_rows)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# To get the unique rows, index position, and occurrence count, you can use:
unique_rows, indices, occurrence_count = np.unique(
    a_2d, axis=0, return_counts=True, return_index=True
)
print(unique_rows)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
print(indices)  # [0 1 2]
print(occurrence_count)  # [2 1 1]

########################################################################################
# Importing and exporting a CSV                                                        #
########################################################################################
print("\nImporting and exporting a CSV\n")

# It's simple to read in a CSV that contains existing information. The best and easiest
# way to do this is to use Pandas.
x_1 = pd.read_csv('music.csv', header=0).values
print(x_1)

# You can also simply select the columns you need:
x_2 = pd.read_csv('music.csv', usecols=['Artist', 'Plays']).values
print(x_2)

# It's simple to use Pandas in order to export your array as well.
a_15 = np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
                 [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
                 [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
                 [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])
df = pd.DataFrame(a_15)
print(df)
#           0         1         2         3
# 0 -2.582892  0.430148 -1.240820  1.595726
# 1  0.990278  1.171510  0.941257 -0.146925
# 2  0.769893  0.812997 -0.950684  0.117696
# 3  0.204840  0.347845  1.969792  0.519928
df.to_csv('pd.csv')
print(pd.read_csv('pd.csv'))
#    Unnamed: 0         0         1         2         3
# 0           0 -2.582892  0.430148 -1.240820  1.595726
# 1           1  0.990278  1.171510  0.941257 -0.146925
# 2           2  0.769893  0.812997 -0.950684  0.117696
# 3           3  0.204840  0.347845  1.969792  0.519928

# You can also save your array with the NumPy `savetxt` method. Or you can open the file
# `np.csv` any time with a text editor!
np.savetxt('np.csv', a_15, fmt='%.2f', delimiter=',', header='1,  2,  3,  4')
