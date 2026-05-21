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