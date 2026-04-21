from functools import reduce

# functions are 'first class citizens' meaning they can:
# 1. you can have other functions as parameters
# 2. you can modify the function
# 3. you can assign a function to a variable
# 4. a function can be returned as a result of another function

# 1. using a function as a parameter:
def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst):
    summation = f(lst)
    return summation

print(higher_order_function(sum_numbers, [1,2,3,4,5]))


# 2. returning a function:
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result)       # shows function name and memory address
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

# Closure (nested functions can access the outer function-- recursion type??)
# Created by nesting a function inside another encapsulating function and then returning the inner function
def multiply_20():
    twenty = 20
    def multiply_num(num):
        return num * twenty
    return multiply_num
closure = multiply_20()
print(closure(10))

# decorators
# add new functionality to an existing object without modifying it
# usually called before the definition of the function you want to decorate
# need an outer function with an inner wrapper function
# structure is like
def to_upper_case_decorator(function):
    def wrapper():
        f = function()
        return f.upper()
    return wrapper

@to_upper_case_decorator # needed above the function you want to decorate
def greeting():
    return 'Hello'
print(greeting())

# multiple decorators can be used but it is important to note that they are applied from top to bottom
# can also accept parameters in wrappers but it is a bit complicated

def location_decorator(function):
    def wrapper(person, job, location):
        function(person, job, location)
        print(f"I live in {location}")
    return wrapper

@location_decorator
def announcement(person, job, location):
    print(f"I am {person}. I work as a {job}.")
announcement('Jonno', 'Computer Vision Engineer', 'Boston')

# built in higher order functions: map() reduce filter
# map(function, iterable)
# map iterates over a list and returns a new one
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

#filer function
# also takes a function and an iterable and goes through the iterable with the criteria of the function (which should return a bool)
# True is kept
numbers = list(range(10))

def keep_evens(num):
    if num%2 == 0:
        return True
    else:
        return False
print(list(filter(keep_evens, numbers)))

# reduce also takes in a function and an iterable but it 'reduces the iterable' as the name suggests
nums = [1,2,3,4,5]
def add_two_nums(x, y):
    return x+y
print(reduce(add_two_nums, nums))