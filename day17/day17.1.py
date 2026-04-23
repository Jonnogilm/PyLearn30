# Try and except blocks are the equivalent to try and catch blocks
# They aim to make programs have "clean exits" when there is an issue
# So, instead of the entire program crashing when there is a str inputed by a user instead of an int it gives a detailed warning message in the log/terminal
# Wrong file name, bad user input, unable to find a file, or a malfunctioning IO device
# If we use try and except, those blocks of code won't raise errors it will just skip the 'try' code
try:
    print(5 + '10')
except:
    print('Something went wrong')

try:
    number = int(input("Enter a number you like: "))
    name = input("What is your name: ")
    print((1/number), 'is your lucky number', name)
except Exception as e:
    print(e)
else:
    print("things went well")
finally:
    print("I always run")

# Packing + Unpacking
# *lst_unpacks    **dict_unpacks
def add_three(a,b,c):
    return a + b + c

lst = [1,6,7]
try:
    add_three(lst)
except Exception as e:
    print(e)
    print(add_three(*lst))

# can use to give functions parameters
range_section = [2, 7]
nums = list(range(*range_section))
print(nums)

# can also be unpacked like this but we already tried doing this much earlier:
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(middle)

# Sometimes you dont know how many parameters are going to be inputed into a given function and that is when you can use packing
def add_all_nums(*nums):
    s = 0
    for num in nums:
        s += num
    return s

lst_2 = (2,3,4,63,3)
print(add_all_nums(*lst_2))

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']