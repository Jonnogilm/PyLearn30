dog = dict()
dog['name'], dog['color'], dog['breed'], dog['legs'], dog['age'] = 'Piper', 'Brown', 'Poodle', 4, 10
print(dog)
student = {'first_name' : 'Tommy', 'last_name' : 'Patricio', 'gender' : 'male', 'age' : 24, 'marital_status' : False, 'skills' : ['Hockey', 'Woodworking', 'Whittling', 'Mountain Biking'], 'country' : 'USA', 'city' : 'Montgomery', 'address' : 50}
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('Swimming')
print(student['skills'])
print(student.keys())
print(student.values())
print(student.items())

student.pop('country')
print(student)
del student