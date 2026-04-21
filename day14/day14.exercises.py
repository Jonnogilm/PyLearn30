from functools import reduce
from countries import countries_list
import string

# Explain the difference between map, filter, and reduce.
    # they all take in a function and an iterable but return different things. map iterates over the iterable and applies the function on each iteration like .upper() to a list of strings. 
    # filter returns a filered iterable according to the specifications made in the function, if the iteration returns True it stays, it is removed on false. an example would be taking out odd numbers. 
    # reduce takes in an iterable and reduces it to a single value according to the function. an example would be sum two numbers over a list of 50 numbers. the output is the sum of them all.

# Explain the difference between higher order function, closure and decorator
    # Higher order functions mean that functions can:
        # 1. Be returned by another function 
        # 2. Be a parameter in another function 
        # 3. you can assign a function to a variable 
        # 4. you cannot modify a function
    # Closure is a nested function that has access to the variables of the parent function even when the parent has finished executing
    # Decorator is used to modify a function without actually rewriting the code
numbers = [1,2,3,4,5,6,7,8,9]
def square(x):
    return x ** 2
numbers_squared = list(map(square, numbers))
print(numbers_squared)

def get_evens(num):
    if num % 2 == 0:
        return True
    else:
        return False

even_numbers = list(filter(get_evens, numbers))
print(even_numbers)

def multiply_two_numbers(x, y):
    return x * y

multiplyed = reduce(multiply_two_numbers, numbers)
print(multiplyed)

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers_2:
    print(number)

#Use map to create a new list by changing each country to uppercase in the countries list
uppercase_countries = list(map(lambda country: country.upper(), countries))
print(uppercase_countries)

#Use map to create a new list by changing each number to its square in the numbers list
numbers_squared_2 = list(map(lambda x: x ** 2, numbers))
print(numbers_squared_2)

#Use map to change each name to uppercase in the names list
names_uppercase = list(map(lambda name: name.capitalize(), names))
print(names_uppercase)

#Use filter to filter out countries containing 'land'.
without_land = list(filter(lambda x: False if 'land' in x else True, countries))
print(without_land)

#Use filter to filter out countries having exactly six characters.
without_six = list(filter(lambda x: False if len(x) == 6 else True, countries))
print(without_six)

#Use filter to filter out countries containing six letters and more in the country list.
without_six_or_over = list(filter(lambda x: False if len(x) >= 6 else True, countries))
print(without_six_or_over)

#Use filter to filter out countries starting with an 'E'
without_e = list(filter(lambda x: False if x[0] == 'E' else True, countries))
print(without_e)

#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
cities = ['Boston', 'Tampa', 'Buffalo', 'Seattle', 'New York', 'Los Angeles']
modified_cities = list(filter(lambda x: False if ' ' in x else True, map(lambda x: x.upper(), cities)))
print(modified_cities)

#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return [reduce(lambda x, y: x + ' ' + y, lst)]
print(get_string_lists(cities))

#Use reduce to sum all the numbers in the numbers list.
def add_all_numbers(numbers):
    return reduce(lambda x, y: x + y, numbers)
print(add_all_numbers(numbers))

#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def produce_sentance(ne_countries):
    return reduce(lambda x, y: x + ', ' + y, ne_countries) + ' are north European countries.'
print(produce_sentance(countries))

#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries():
    i = 0
    num_of_land = 0
    num_of_ia = 0
    num_of_stan = 0

    for country in countries_list:
        if 'land' in country:
            num_of_land += 1
        if 'stan' in country:
            num_of_stan += 1
        if 'ia' in country:
            num_of_ia += 1
    return 'ia = ' + str(num_of_ia) + ', land = ' + str(num_of_land) + ', stan = ' + str(num_of_stan)
print(categorize_countries())
#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def dict_of_countries():
    list_of_char = list(string.ascii_uppercase)
    init_list = [0] * len(list_of_char)
    tracking = dict(zip(list_of_char, init_list))
    for country in countries_list:
        tracking[country[0:1]] += 1
    return tracking
print(dict_of_countries())
#Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries():
    return countries[:10]
print(get_first_ten_countries())
#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
    return countries[-10:]
print(get_last_ten_countries)