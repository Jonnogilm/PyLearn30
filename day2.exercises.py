# Day 2: 30 Days of python programming
import math

first_name = 'Bob'
last_name = 'Smith'
full_name = 'Bob Smith'
country = "Azerbijan"
city = 'Kelp'
age = 18
year = 2026
is_married = True
is_true = False
is_light_on = True
is_in_school, mothers_name, hobbies = True, 'Mauritiaus', ('Soccer', 'Math', 'Swimming')

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(is_in_school))
print(type(mothers_name))
print(type(hobbies))

print(len(first_name))
print(len(first_name)-len(last_name))

num_one = 5
num_two = 4
total = num_one+num_two
diff = num_one-num_two
product = num_two*num_one
division = num_one/num_two
remainder = num_two%num_one
exp = num_one**num_two
floor_divison = num_one//num_two

r = 30
area_of_circle = r**2 * math.pi
circum_of_circle = 2 * math.pi * r
print(area_of_circle)
print(circum_of_circle)

input_radius = float(input('Please input a radius'))
area_of_circle = pow(input_radius, 2) * math.pi
print(f'Area of {input_radius} is: ', area_of_circle)