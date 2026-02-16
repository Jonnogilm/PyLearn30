# functions are named with def
# you can pass in parameters (same as java exept this time if the passed in value matched the key the order doesnt matter
def add_two_numbers (num1, num2):
    return num1+num2

print(add_two_numbers(2,4))
print(add_two_numbers(num1 = 5, num2= 2))

# there is no difference between void and having a return type only that the function returns something
def print_hello():
    print("Hello World")

print_hello()

# give the variable a value if you want a default if no params are passed (name = "Joe")
# arbitrary number of arguments use (*args)
# if your keys line up with named arguments you can use **
def greet(name, location):
    print('Hi',name,'how is the weather in', location)
my_dict = {'name': 'Alice', 'location': 'New York'}
greet(**my_dict)

# to accept an arbitrary number of named arguments it is **args
# you can also pass functions as a parameter of another function