# list comprehension is a shorter way to make a list
'''expression for i in iterable if condition'''

language = "Python"
lst = [i for i in language]
print(lst)

# can return squares
# can return tuples
# can add if statements at the end to modify what gets taken
# can flatten a 2D array
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

'''for rows in list_of_lists:
    for number in rows:
        print(number)'''

# lambda lists are small anonymous functions with unlimited number of arguments but can only have one expression
# the lambda function does not have a name
# to create it you write lambda, then params, then expression
# return is implicit
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(1, 2, 3))

# Self invoking lambda function
(lambda a, b: a + b)(2,3) #need to write print() around to see it

# can also use within a function
def power(x):
    return lambda n : x ** n
# called by:
power(2)(3)