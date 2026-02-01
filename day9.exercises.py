# Same as any other language exept no syntax is easier
# shorthand: code if condition else code
# && is replaced by and so if condition and condition: code
# or is ||

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are old enough to drive.")
else:
    print("Please wait", 18-user_age, "year(s) to drive.")

my_age = 24

if my_age > user_age:
    if my_age-user_age > 1:
        print("You are", my_age-user_age, "years younger than me.")
    else:
        print("You are", my_age-user_age, "year younger than me.")
else:
    if my_age-user_age < -1:
        print("You are", user_age-my_age, "years older than me.")
    else:
        print("You are", user_age-my_age, "year older than me.")


a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(a, "is greater than", b)
elif b > a:
    print(b, "is greater than", a)
else:
    print(a, "is equal to", b)


grade = int(input("Enter your grade: "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

Autumn = ["September", "October", "November"]
Winter = ["December", "January", "February"]
Spring = ["March", "April", "May"]
Summer = ["June", "July", "August"]

month = input("Input a month: ")

if month in Autumn:
    print(month, "is in Autumn")
elif month in Winter:
    print(month, "is in Winter")
elif month in Spring:
    print(month, "is in Spring")
elif month in Summer:
    print(month, "is in Summer")

fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input("Pick a fruit: ")
if user_fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(user_fruit)
    print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    print((len(person['skills'])//2))
    if person['skills'].index('Python') > -1:
        print("Python")