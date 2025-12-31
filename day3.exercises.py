import math

# Day 3 exercises
age = 34
height = 6.0
complex_number = 3 + 1j

triangle_base = int(input('Enter base: '))
triangle_height = int(input('Enter height: '))
triangle_area = 0.5 * triangle_base * triangle_height

print('The area of the triangle is ', triangle_area)

side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_a + side_b + side_c

print('The perimeter of the triangle is ', perimeter)

rect_width = int(input('Width: '))
rect_length = int(input('Height'))
rect_area = rect_length * rect_width
rect_perimeter = 2 * (rect_length + rect_width)

print(f'The area of the rectangle is {rect_area}')
print(f'The perimeter of the rectangle is {rect_perimeter}')

radius = float(input('Define a radius: '))
pi = 3.14
circle_area = radius * pi * radius
circle_circumference = 2 * pi * radius

print('Circle area is: ', circle_area)
print('Circle circumference is: ', circle_circumference)

# Given line: y = 2x - 2
m = 2
b = -2

slope_1 = m
y_int_1 = (0, b)
x_int_1 = (-b/m, 0)

# Given points: (2,2) and (6,10)

x1, y1 = 2, 2
x2, y2 = 6, 10

slope_2 = (y2-y1)/(x2-x1)
distace_2 = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print('Difference in slopes: ', slope_1-slope_2)

x = 4
y = 3

result = x**2 + 6*x + 9 - y

print(len('dragon') > len('python'))
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'python' and 'on' not in 'dragon')

python_length = len('python')
python_length = str(float(python_length))
print(python_length)

num = 54
is_even = 54 % 2

floor = 7 // 3 == int(2.7)
print(floor)

check_type = type('10') == type(10)
print(check_type)

check_equals = int(float('9.8')) == 10
print(check_equals)

hours = int(input('Enter hours: '))
rate = float(input("Enter rate per hour: "))
print('Your weekly earning is ', hours*rate)

years_lived = int(input('Enter the number of years you have lived: '))
print(f'You have lived for {years_lived*60*60*24*365.25} seconds.')

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')