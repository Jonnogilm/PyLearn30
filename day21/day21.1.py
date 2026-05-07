# classes
# python is an object oriented programing language so everything is stored and processed as an object
# this means that even strings, ints, floats and more are simply a built in class
# classes are the boilerplate to make new objects, like a constructor in java
# class defines the attributes and behaviors of the object while the object is an instant of the class (represents it)
class SomeFunction:
    pass
print(SomeFunction) # prints class type "SomeFunction"

# create an object by similar flow to java:
p = SomeFunction()
print(p) # prints the memory reference along with the object type

# now to use constructors as you do in java
# you use the base __init__ function
class OtherFunction:
    def __init__(self, name): # reference to the current instance of the class
        self.name = name #similar to the this.name = name that you do in java
OT = OtherFunction("Banana")
print(OT.name)

# python doesn't allow the standard overloaded constructor but you can give default values to parameters if nothing is given
# can avoid errors if the user doesn't add all the parameters
# can also update object variables through functions defined in the class
class Greeting:
    def __init__(self, firstname="John", age=20):
        self.firstname = firstname
        self.age = age
        self.skills = []
    def return_string(self):
        return f'Hi {self.firstname}, you are {self.age}. You have the following skills: {self.skills}'
    
    def add_skills(self, *skill):
        self.skills.append(skill)
g = Greeting()
greeting_personalized = Greeting("Jonno", 18)
g.add_skills("PHP")
g.add_skills("Java", "Python")
print(g.return_string())
print(greeting_personalized.return_string())

# inheritence is a way to take a parent class and inherit the same properties and methods
# you use it as if it were an object being passed into a function
# called child
class Child(Greeting):
# as a child class you do not need to call the init function but you can though you need to use the super
# it can help you change the constructor as well by doing
    def __init__(self, firstname="John", age=20, gender='male'):
        self.gender = gender
        super().__init__(firstname, age)

    def print_gender(self):
        return self.gender
greeting_child = Child()
print(greeting_child.return_string())
print(greeting_child.print_gender())
