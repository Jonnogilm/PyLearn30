import math

def add_two_numbers (num1, num2):
    return num1+num2
print(add_two_numbers(2,5))

def area_of_circle (radius):
    return radius*radius*3.14
print(area_of_circle(4))

def add_all_nums (*nums):
    total = 0
    
    for num in nums:
        if type(num) != int:
            return "Please pass in integers"
        total += num
    return num
print(add_all_nums(1,4,5,6,7,3,24))

def convert_celsius_to_fahrenheit (temp_in_celsius):
    return (temp_in_celsius*(9/5))+32
print(convert_celsius_to_fahrenheit(100))

def check_season(month):
    autumn = ["September", "October", "November"]
    winter = ["December", "January", "February"]
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"] 
    if month in autumn:
        return "Autumn"
    if month in winter:
        return "winter"
    if month in summer:
        return "Summer"
    if month in spring:
        return "Spring"
print(check_season("March"))

def calculate_slope (point1,point2):
    return (point2[1]-point1[1])/(point2[0]-point1[0])
print(calculate_slope([2,3],[5,17]))

def solve_quadratic_eqn (a,b,c):
    sol1 = (-b+math.sqrt(b**2-(4*a*c)))/(2*a)
    sol2 = (-b-math.sqrt(b**2-(4*a*c)))/(2*a)
    return "x =",sol1,",",sol2
print(solve_quadratic_eqn(1,4,4))

array1 = [1, 2, 3, 4, 5]
def print_list (array):
    for i in array:
        print(i, sep=" ," ,end="")
print_list(array1)
print("")

def reverse_list (array):
    return array[::-1]
print(reverse_list(array1))

list1 = ['potato', 'tomato', 'mango', 'milk']
def capitalize_list_items (lst):
    i = 0;
    while i < len(lst):
        lst[i] = lst[i].capitalize()
        i += 1
    return lst
print(capitalize_list_items(list1))

def add_item (lst, item):
    lst.append(item)
    return lst
print(add_item(list1, 'Eggs'))

def remove_item (lst, item):
    lst.remove(item)
    return lst
print(remove_item(list1, 'Milk'))

def sum_of_numbers (num):
    sum = 0
    num_list = range(num+1)
    for nums in num_list:
        sum += nums
    return sum
print(sum_of_numbers(5))
print(sum_of_numbers(100))

def sum_of_odds (num):
    total = 0
    for i in range(num+1):
        if i%2 == 0:
            continue
        total+=i
    return total
print(sum_of_odds(10))

def sum_of_evens (num):
    total = 0
    for i in range(num+1):
        if i%2 != 0:
            continue
        total+=i
    return total
print(sum_of_evens(10))

#level 2
def evens_and_odds (num):
    evens = 0
    odds = 0
    for i in range(num+1):
        if i%2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds
print(evens_and_odds(22200))

def factorial (whole_num):
    product = 1
    for i in range(1, whole_num+1):
        product *= i
    return product
print(factorial(10))

def is_empty (param):
    if len(param) < 1:
        return True
    else:
        return False
print(is_empty(""))

def calculate_mean (num_lst):
    sum = 0
    nums = len(num_lst)
    for i in num_lst:
        sum += i
    return sum/nums

def calculate_median (num_lst):
    return sorted(num_lst)[len(num_lst)//2]

def calculate_mode (num_lst):
    max = 0
    count = {}
    for x in num_lst:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    for value in count:
        if count[value] > max:
            max = value
    return max
data = [4,1,2,2,3,3,3,4,4,4,5]
print(calculate_mode(data))

def greet (name = "Guest"):
    print("Hello,",name)
greet("Jonno")
greet()

def show_args (**args):
    print("Recived: ", end=" ")
    for k,v in args.items():
        print(k, ", ", v,".", sep=None, end=None)
show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny