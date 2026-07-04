# basic statistics knowledge is extreamly important as it tells how to collect, organize, display, and interpret data
# useful for applications from ML to website traffic data
# data is any set of characters that is gathered and translated for some purpose, usually analysis. 
# without context it doesn't serve any purpose to humans or computers

# data can be provided or created
# there is structured and unstructured data

# built in statistics module is supposed to be at the level of graphing and scientfic calculators, not replacing NumPy and Matlab

# Numpy is the core of scientific computing for python, gives high-performance multidimentsional array objects, and other tools for working with arrays
import numpy as np

python_list = [1,2,3,4,5]
print(type(python_list))

py_two_dimensional = [[1,2,3],[4,5,6],[7,8,9]]
print(type(py_two_dimensional))
print(py_two_dimensional)

# crate Np array from python list
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

numpy_2 = np.array(python_list, dtype=float)
print(numpy_2)

numpy_bool_array = np.array([0,0,1,-1,0,1], dtype=bool)
print(numpy_bool_array, sep=',')

#multidimentional is the same np.array
# converting numpy array to lst
np_to_lst = numpy_array_from_list.tolist()
print(type(np_to_lst))
print(np_to_lst)

# can also do the same np.array with a tuple
# .shape() method returns a tuple of the shape of the numpy array with the first number being the rows and the second the columns
two_dimensional_numpy = np.array(py_two_dimensional)
shape_of2 = two_dimensional_numpy.shape
print(shape_of2)
row, col = shape_of2
print(f'The array has {row} rows and {col} columns.')

# use dtype to get type of a numpy array
# use size to get the number of items in an array
print(two_dimensional_numpy.size)

# You can also perform mathmatical operations on the entire array by using numpy
np_array_from_list = np.array([1,2,3,4,5])
print(f"original: {np_array_from_list}")
ten_plus = np_array_from_list +10
print(f"new: {ten_plus}")

# same with all the others -, *, /, %, //, **
# much quicker than looping through the enire list and adding one by one somehow
print(ten_plus.dtype)

# can change the dtype by doing dtype = "type"
# getting items from a numpy array is the exact same
numpy_new_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"first row: {numpy_new_array[0]}")
print(f"middle value: {numpy_new_array[1][1]}")

# you can slice the array by doing numpy_array[range, range]
numpy_smaller = numpy_new_array[0:2, 0:2]
print(numpy_smaller)

#reverse the entire array using ::
two_dimension_flipped = numpy_new_array[::]
print(two_dimension_flipped)

# flip columns and rows as you would with ::-1
# np.zeros to make an array with all zeros or np.ones
array_of_ones = np.ones((3,3), dtype = int)
print(array_of_ones)

# can also reshape with numpy:
first = np.array([[1,2,3], [4,5,6]])
print(first)
print(first.flatten())

# np.random for a more powerful random number generator than the built in math one
#mu, sigma, size of the list
print(np.random.normal(79, 15, 80))


import matplotlib.pyplot as plt
import seaborn as sns

# you can also use numpy to make matricies which is probably now what it is used the most for
# matricies in numpy let you do inversing easily but you are restricted to 2D
matrix = np.matrix(np.ones((4,4), dtype = float))
print(matrix)
 
# with np you can also do all the normal statistical calculations
# project them with matplotlib
np_normal = np.random.normal(5, 0.5, 1000)
plt.hist(np_normal, color="gray", bins=30)
plt.show()

#lin alg
f = np.array([1,2,3])
g = np.array([4,5,3])
print(np.dot(f, g))

# use matmul for matrix multiplication
# use .I for inverse and use .det for the determinent
day = np.array([1,2,3,4,5])
temp = np.array(day * 10 + 2)

plt.plot(day, temp)
plt.xlabel("Day")
plt.ylabel("Temp")
plt.title("Tempurature by Day")
plt.xticks(np.arange(0, 5, step=0.5))
plt.show()

# faster because all the operations are vectorized so instead of modifying all the values individually it is basically a transformation of the entire vector in space
# cannot change size like lists in java
# takes much less space as well

