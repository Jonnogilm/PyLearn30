# syntax error is the most common: typical caught by interpreter, the interpreter often offers suggestions
# print 'Hello World' -------- SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?

# Name error is when you dont define a variable and then use it.
# VSC definitly catches this before the interpreter but good to know the interpreter can find it too: NameError: name 'age' is not defined

# Index error: like java indexOutOfBounds error
# Ex. IndexError: list index out of range

# Module not found error when importing functions or packages: 
# ModuleNotFoundError: No module named 'maths'

# Attribute error is similar but if there is no attribute of the module with the given name you tried
# Like saying math.PI instead of math.pi

# Key error is when you try to access a slot of a dictionary with a key that doesn't exist
# I'm pretty sure you can resolve this if you instead use get() or a try catch block

# Type error is when you have an unsupported operation like trying to add a str and an int
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Need to cast

# Import error is when you get the function from the module wrong
# ImportError: cannot import name 'power' from 'math'

# ValueError: Can't cast a string or number because it contains some illigal expression
# ValueError: invalid literal for int() with base 10: '12a'

# Division by zero is pretty self explanitory